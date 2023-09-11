from rest_framework import serializers

from .models import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('title', 'salary_max', 'company', 'place', 'experience', 'type', 'tasks', 'require')


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        # Исключение поля
        exclude = ('title',)


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
