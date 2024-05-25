from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name', 'last_name', 'surname',
            'date_of_birth', 'citizenship', 'region',
            'city', 'about', 'about_work', 'telegram',
            'website', 'phone_number', 'avatar',
        ]


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'surname',
            'date_of_birth', 'citizenship', 'region',
            'city', 'about', 'about_work', 'telegram',
            'website', 'phone_number', 'avatar',
        ]


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'usertype', 'avatar']


class UserChatSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'avatar', 'last_login'
        ]
