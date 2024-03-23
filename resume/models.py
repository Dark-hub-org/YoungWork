from django.db import models
from profiles.models import Applicant
from jobs.models import Vacancies
from django.contrib.postgres.fields import ArrayField
from accounts.models import User
import uuid
from datetime import datetime as datetime


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume_title = models.CharField('Название', null=True, max_length=100, default='')
    salary = models.BigIntegerField('Зарплата', blank=True, null=True, default=0)
    employ = ArrayField(models.CharField(max_length=100), verbose_name="Тип занятости", default=list, blank=True,
                        null=True)
    skills = ArrayField(models.CharField('Навыки', max_length=100), verbose_name="Навыки", default=list, blank=True,
                        null=True)
    quality = ArrayField(models.CharField(max_length=100), verbose_name="Качества", default=list, blank=True, null=True)
    experience = models.CharField('Опыт', blank=True, null=True, default='')
    about_us = models.TextField('О вам', blank=True, null=True, default='')

    timestamp = models.DateField('Дата вызова', auto_now_add=False, auto_now=True)
    created_by = models.ForeignKey(Applicant, verbose_name="Создатель", related_name='applicant_resume',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy = models.ManyToManyField(Vacancies, verbose_name="Вакансия", related_name='vacancies')

    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name="Создатель", related_name='user_favorites',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
