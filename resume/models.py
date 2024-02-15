from django.db import models
from profiles.models import Applicant
from jobs.models import Vacancies
from django.contrib.postgres.fields import ArrayField
import uuid
from datetime import datetime as datetime


class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume_title = models.CharField(null=True, max_length=100, default='')
    salary = models.BigIntegerField(blank=True, null=True, default=0)
    employ = ArrayField(models.CharField(max_length=100), default=list, blank=True, null=True)
    skills = ArrayField(models.CharField(max_length=100), default=list, blank=True, null=True)
    quality = ArrayField(models.CharField(max_length=100), default=list, blank=True, null=True)
    experience = models.CharField(blank=True, null=True, default='')
    about_us = models.TextField(blank=True, null=True, default='')

    timestamp = models.DateField(auto_now_add=False, auto_now=True)
    created_by = models.ForeignKey(Applicant, related_name='applicant_summary', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # vacancy = models.ManyToManyField(Vacancies, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Applicant, related_name='applicant_favorites', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
