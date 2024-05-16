from django.http import JsonResponse
from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from djangochannelsrestframework.observer import model_observer

from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer

from accounts.models import User
from accounts.serializers import UserSerializer


class ChatConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    lookup_field = "pk"

    async def disconnect(self, code):
        if hasattr(self, "room_subscribe"):
            await self.remove_user_from_room(self.room_subscribe)
        await super().disconnect(code)

    @action()
    async def join_room(self, pk, **kwargs):
        self.room_subscribe = pk
        await self.add_user_to_room(pk)

    @action()
    async def leave_room(self, pk, **kwargs):
        await self.remove_user_from_room(pk)

    @action()
    async def create_message(self, message, **kwargs):
        room = await self.get_room(pk=self.room_subscribe)
        await database_sync_to_async(ConversationMessage.objects.create)(
            conversation=room,
            created_by=self.scope["user"],
            body=message
        )

    @action()
    async def subscribe_to_messages_in_room(self, pk, **kwargs):
        await self.message_activity.subscribe(room=pk)

    @model_observer(ConversationMessage)
    async def message_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @message_activity.groups_for_signal
    def message_activity(self, instance: ConversationMessage, **kwargs):
        yield f'room__{instance.conversation_id}'
        yield f'pk__{instance.pk}'

    @message_activity.groups_for_consumer
    def message_activity(self, room=None, **kwargs):
        if room is not None:
            yield f'room__{room}'

    @message_activity.serializer
    def message_activity(self, instance: ConversationMessage, action, **kwargs):
        return dict(data=ConversationMessageSerializer(instance).data, action=action.value, pk=instance.pk)

    @database_sync_to_async
    def get_room(self, pk):
        return Conversation.objects.get(pk=pk)

    @database_sync_to_async
    def conversation_get_or_create(self, pk):
        user = User.objects.get(pk=pk)
        current_user = self.scope["user"]

        conversation = Conversation.objects.filter(users=current_user).filter(users=user).first()
        if not conversation:
            conversation = Conversation.objects.create()
            conversation.users.add(current_user, user)
            conversation.save()
        elif current_user in conversation.history.all():
            conversation.users.add(current_user)
            conversation.history.remove(current_user)

        serializer = ConversationDetailSerializer(conversation)
        return JsonResponse(serializer.data, safe=False)

    @database_sync_to_async
    def current_users(self, room: Conversation):
        return [UserSerializer(user).data for user in room.users.all()]

    @database_sync_to_async
    def remove_user_from_room(self, pk):
        user = self.scope["user"]
        room = Conversation.objects.get(pk=pk)
        room.users.remove(user)

    @database_sync_to_async
    def add_user_to_room(self, pk):
        user = self.scope["user"]
        room = Conversation.objects.get(pk=pk)
        if not room.users.filter(pk=user.pk).exists():
            room.users.add(user)
