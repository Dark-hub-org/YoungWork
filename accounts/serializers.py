from rest_framework import serializers

from .models import MyUser


class MyUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"
