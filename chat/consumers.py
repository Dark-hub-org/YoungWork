from channels.db import database_sync_to_async
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin, action
from .serializers import (
    ConversationSerializer, ConversationMessageSerializer,
    ConversationDetailSerializer, ResumeConDetailSerializer,
    VacancyConDetailSerializer
)

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from .models import Conversation, ConversationMessage
from accounts.serializers import UserChatSerializer
from resume.models import Resume
from jobs.models import Vacancies

import json


class ChatConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    lookup_field = "pk"

    async def disconnect(self, close_code):
        user = self.scope["user"]
        conversation = Conversation.objects.filter(users=user).first()
        if conversation:
            self.chat_name = str(conversation.id)
            await self.channel_layer.group_discard(self.chat_name, self.channel_name)

    @action()
    async def create_message(self, message, conversation_id, **kwargs):
        user = self.scope["user"]
        try:
            conversation = await database_sync_to_async(
                lambda: Conversation.objects.filter(id=conversation_id, users=user).first()
            )()

            if not conversation:
                await self.send_json({"success": False, "message": "Беседа не найдена или доступ запрещен."})
                return

            sent_to = None
            users = await database_sync_to_async(lambda: list(conversation.users.all()))()

            for participant in users:
                if participant != user:
                    sent_to = participant
                    break

            message_instance = await self.create_conversation_message(
                conversation=conversation,
                created_by=user,
                body=message,
                sent_to=sent_to
            )
            chat_name = str(conversation_id)
            await self.channel_layer.group_send(
                f"{chat_name}",
                {
                    "type": "chat_message",
                    "message": ConversationMessageSerializer(message_instance).data,
                }
            )

        except Exception as e:
            await self.send_json({"success": False, "message": f"Произошла ошибка: {str(e)}"})

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'action': 'new_message',
            'message': message,
        }))

    @database_sync_to_async
    def create_conversation_message(self, conversation, created_by, body, sent_to):
        return ConversationMessage.objects.create(
            conversation=conversation,
            created_by=created_by,
            body=body,
            sent_to=sent_to,
        )

    @action()
    async def conversation_list(self, **kwargs):
        user = self.scope["user"]
        conversations = await self.get_conversations_for_user(user)
        serialized_data = []

        for conversation in conversations:
            users = await self.exclude_user(conversation.users, user.id)
            history = await self.exclude_user(conversation.history, user.id)
            last_message = await self.get_last_message(conversation)
            unread_count = await self.get_unread_count(conversation)
            serialized_data.append({
                'id': str(conversation.id),
                'users': UserChatSerializer(users, many=True).data,
                'history': UserChatSerializer(history, many=True).data,
                'last_message': ConversationMessageSerializer(last_message).data if last_message else None,
                'unread_count': unread_count,
            })

        await self.send_json({'action': 'conversation_list', 'data': serialized_data})

    @database_sync_to_async
    def get_conversations_for_user(self, user):
        return list(Conversation.objects.filter(users=user))

    @database_sync_to_async
    def exclude_user(self, queryset, user_id):
        return list(queryset.exclude(id=user_id))

    @database_sync_to_async
    def get_last_message(self, conversation):
        return conversation.messages.order_by('-created_at').first()

    @database_sync_to_async
    def get_unread_count(self, conversation):
        return conversation.messages.filter(is_read=False).count()

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
        user = self.scope["user"]
        try:
            conversation = await database_sync_to_async(
                lambda: Conversation.objects.filter(users=user).get(pk=pk)
            )()
            self.chat_name = str(conversation.id)
            await self.channel_layer.group_add(self.chat_name, self.channel_name)

            if usertype == "employer":
                resume = await database_sync_to_async(
                    lambda: Resume.objects.filter(created_by=user_id).first()
                )()
                serialized_data = {
                    'conversation': ConversationDetailSerializer(conversation).data,
                    'resume': ResumeConDetailSerializer(resume).data if resume else None
                }
            else:
                vacancy = await database_sync_to_async(
                    lambda: Vacancies.objects.filter(created_by=user_id).first()
                )()
                serialized_data = {
                    'conversation': ConversationDetailSerializer(conversation).data,
                    'vacancy': VacancyConDetailSerializer(vacancy).data if vacancy else None
                }

            serialized_data['conversation']['id'] = str(conversation.id)
            serialized_data['conversation']['users'] = [str(user) for user in conversation.users.all()]

            await self.send_json({'action': 'conversation_detail', 'data': serialized_data})
        except Conversation.DoesNotExist:
            await self.send_json({"success": False, "message": "Беседа не найдена."})
        except Exception as e:
            await self.send_json({"success": False, "message": f"Произошла ошибка: {str(e)}"})
