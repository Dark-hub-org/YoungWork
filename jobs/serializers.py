from rest_framework import serializers

from .models import Vacancies, Response


class VacanciesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class VacanciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class ResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = "__all__"
