from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Vacancies, Events


class VacanciesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class VacanciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = "__all__"


class EventsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
