from rest_framework import serializers

from .models import Vacancies


class VacanciesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class VacanciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"
