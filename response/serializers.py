from rest_framework import serializers
from .models import Response


class ResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = "__all__"
