from channels.db import database_sync_to_async
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from djangochannelsrestframework.observer import model_observer

from .models import Conversation, ConversationMessage

from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer, \
    ResumeConDetailSerializer, VacancyConDetailSerializer
from accounts.models import User
from jobs.models import Vacancies
from resume.models import Resume
from accounts.serializers import UserSerializer, UserChatSerializer


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

    @action()
    async def conversation_list(self, **kwargs):
        conversations = await database_sync_to_async(Conversation.objects.filter)(users=self.scope["user"])
        serialized_data = []

        for conversation in conversations:
            users = conversation.users.exclude(id=self.scope["user"].id)
            pk = conversation.id
            conversation_last = await database_sync_to_async(Conversation.objects.get)(pk=pk)
            message = await database_sync_to_async(conversation_last.messages.all)()
            history = conversation.history.exclude(id=self.scope["user"].id)
            last_message = await database_sync_to_async(message.order_by('-created_at').first)()
            unread_count = await database_sync_to_async(message.filter(is_read=False).count)()
            serialized_data.append({
                'id': conversation.id,
                'users': UserChatSerializer(users, many=True).data,
                'history': UserChatSerializer(history, many=True).data,
                'last_message': ConversationMessageSerializer(last_message).data if last_message else None,
                'unread_count': unread_count,
            })

        await self.send_json(serialized_data)

    @action()
    async def conversation_remove(self, pk, **kwargs):
        try:
            conversation = await database_sync_to_async(Conversation.objects.get)(id=pk)
            user_to_remove = self.scope["user"]
            await database_sync_to_async(conversation.users.remove)(user_to_remove)
            await database_sync_to_async(conversation.history.add)(user_to_remove)
            await self.send_json({"success": True, "message": "Пользователь вышел из беседы!"})
        except Conversation.DoesNotExist:
            await self.send_json({"success": False, "message": "Беседа с указанным ID не существует."})
        except Exception as e:
            await self.send_json({"success": False, "message": f"Произошла ошибка: {str(e)}"})

    @action()
    async def conversation_detail(self, pk, user_id, usertype, **kwargs):
        conversation = await database_sync_to_async(Conversation.objects.filter(users=self.scope["user"]).get)(pk=pk)

        if usertype == "employer":
            resume = await database_sync_to_async(Resume.objects.filter(created_by=user_id).first)()
            serialized_data = {
                'conversation': ConversationDetailSerializer(conversation).data,
                'resume': ResumeConDetailSerializer(resume).data
            }
        else:
            vacancy = await database_sync_to_async(Vacancies.objects.filter(created_by=user_id).first)()
            serialized_data = {
                'conversation': ConversationDetailSerializer(conversation).data,
                'vacancy': VacancyConDetailSerializer(vacancy).data
            }

        await self.send_json(serialized_data)

    @action()
    async def conversation_get_or_create(self, pk, **kwargs):
        user = await database_sync_to_async(User.objects.get)(pk=pk)
        current_user = self.scope["user"]

        conversation = await database_sync_to_async(
            Conversation.objects.filter(users=current_user).filter(users=user).first)()
        if not conversation:
            conversation = await database_sync_to_async(Conversation.objects.create)()
            await database_sync_to_async(conversation.users.add)(current_user, user)
            await database_sync_to_async(conversation.save)()
        elif current_user in await database_sync_to_async(conversation.history.all)():
            await database_sync_to_async(conversation.users.add)(current_user)
            await database_sync_to_async(conversation.history.remove)(current_user)

        serializer = ConversationDetailSerializer(conversation)
        await self.send_json(serializer.data)

    @action()
    async def conversation_send_message(self, pk, message, **kwargs):
        conversation = await database_sync_to_async(Conversation.objects.filter(users=self.scope["user"]).get)(pk=pk)

        sent_to = None
        for user in await database_sync_to_async(conversation.users.all)():
            if user != self.scope["user"]:
                sent_to = user

        conversation_message = await database_sync_to_async(ConversationMessage.objects.create)(
            conversation=conversation,
            body=message,
            created_by=self.scope["user"],
            sent_to=sent_to
        )

        serializer = ConversationMessageSerializer(conversation_message)
        await self.send_json(serializer.data)

    @action()
    async def read_message(self, conversation_id, **kwargs):
        await database_sync_to_async(ConversationMessage.objects.filter(conversation=conversation_id).update)(
            is_read=True)
        await self.send_json({'message': 'message read'})

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
