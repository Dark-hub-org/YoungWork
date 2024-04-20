from django.db import models
from profiles.models import Applicant
from django.contrib.postgres.fields import ArrayField
import uuid


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
    about_us = models.TextField('О ваc', blank=True, null=True, default='')
    active = models.BooleanField(default=True)

    timestamp = models.DateField('Дата вызова', auto_now_add=False, auto_now=True)
    created_by = models.ForeignKey(Applicant, verbose_name="Создатель", related_name='applicant_resume',
                                   on_delete=models.CASCADE)

    avatar = models.CharField('Аватар', null=True, blank=True)
    first_name = models.CharField('Имя', blank=True, null=True, max_length=100, default='')
    last_name = models.CharField('Фамилия', blank=True, null=True, max_length=100, default='')
    surname = models.CharField('Отчество', blank=True, null=True, max_length=100, default='')
    telegram = models.CharField('Телеграм', blank=True, null=True, max_length=100, default='')
    website = models.CharField('Сайт', blank=True, null=True, max_length=100, default='')
    phone_number = models.CharField('Номер телефона', blank=True, null=True, max_length=100, default='')
    date_of_birth = models.CharField('Дата рождения', blank=True, null=True, default='', help_text="Пример: 1999-10-12")

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.id}'
