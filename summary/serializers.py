from rest_framework import serializers

from .models import Summary


class SummaryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = "__all__"


class SummaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = "__all__"
