from rest_framework import serializers
from .models import *


class DampUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DampUser
        fields = "__all__"


class DampUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DampUser
        fields = "__all__"
