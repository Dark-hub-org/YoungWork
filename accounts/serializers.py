from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
