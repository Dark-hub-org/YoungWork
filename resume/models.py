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
    about_us = models.TextField('О вам', blank=True, null=True, default='')
    active = models.BooleanField(default=True)

    timestamp = models.DateField('Дата вызова', auto_now_add=False, auto_now=True)
    created_by = models.ForeignKey(Applicant, verbose_name="Создатель", related_name='applicant_resume',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.id}'
