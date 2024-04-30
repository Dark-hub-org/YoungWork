from rest_framework import serializers

from accounts.serializers import UserChatSerializer

from .models import Conversation, ConversationMessage


class ConversationSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        user_to_exclude_id = self.context.get('user_id_to_exclude')
        return UserChatSerializer(obj.users.exclude(id=user_to_exclude_id), many=True).data

    class Meta:
        model = Conversation
        fields = ('id', 'users',)


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserChatSerializer(read_only=True)
    created_by = UserChatSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = ConversationMessage
        fields = ('id', 'sent_to', 'created_by', 'created_at', 'body',)


class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConversationMessageSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'created_at', 'messages',)
