from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes

from accounts.models import User

from .models import Conversation, ConversationMessage
from .serializers import UserChatSerializer, ConversationDetailSerializer, ConversationMessageSerializer


@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users=request.user)
    serialized_data = []

    for conversation in conversations:
        users = conversation.users.exclude(id=request.user.id)
        history = conversation.history.exclude(id=request.user.id)
        serialized_data.append({
            'id': conversation.id,
            'users': UserChatSerializer(users, many=True).data,
            'history': UserChatSerializer(history, many=True).data,
        })

    return JsonResponse(serialized_data, safe=False)


@api_view(['DELETE'])
def conversation_remove(request, pk):
    try:
        conversation = Conversation.objects.get(id=pk)
        user_to_remove = User.objects.get(id=request.user.id)
        conversation.users.remove(user_to_remove)
        conversation.history.add(user_to_remove)
        return Response({"success": True, "message": "Пользователь успешно удален из беседы."})
    except Conversation.DoesNotExist:
        return Response({"success": False, "message": "Беседа с указанным ID не существует."})
    except User.DoesNotExist:
        return Response({"success": False, "message": "Пользователь с указанным ID не существует."})
    except Exception as e:
        return Response({"success": False, "message": f"Произошла ошибка: {str(e)}"})


@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=pk)
    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def conversation_get_or_create(request, pk):
    user = User.objects.get(pk=pk)
    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(users__in=list([user]))
    conversations_history = Conversation.objects.filter(history__in=list([request.user])).filter(users__in=list([user]))

    if conversations.exists():
        conversation = conversations.first()
    elif conversations_history.exists():
        conversation = Conversation.objects.filter(history__in=list([request.user])).filter(
            users__in=list([user])).get()
        conversation.users.add(request.user)
        conversation.history.remove(request.user)
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerializer(conversation)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def conversation_send_message(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(pk=pk)

    for user in conversation.users.all():
        if user != request.user:
            sent_to = user

    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get('body'),
        created_by=request.user,
        sent_to=sent_to
    )

    serializer = ConversationMessageSerializer(conversation_message)

    return JsonResponse(serializer.data, safe=False)
