from rest_framework import serializers

from .models import Resume, Favorites


class ResumeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class ResumeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class FavoritesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"
