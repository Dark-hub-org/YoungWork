from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'body', 'type_of_notification', 'is_read', 'vacancy', 'created_for']
