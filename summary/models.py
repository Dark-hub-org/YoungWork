from django.db import models
from profiles.models import Applicant
from jobs.models import Vacancies
import uuid


class Summary(models.Model):
    summary_title = models.CharField(null=True, max_length=100, default='')
    type = models.CharField(blank=True, null=True, default='')
    skills = models.CharField(blank=True, null=True, max_length=100, default='')
    quality = models.CharField(blank=True, null=True, max_length=100, default='')
    experience = models.CharField(blank=True, null=True, default='')
    about_us = models.TextField(blank=True, null=True, default='')
    created_by = models.ForeignKey(Applicant, related_name='applicant_summary', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # vacancy = models.ManyToManyField(Vacancies, blank=True)
    created_by = models.ForeignKey(Applicant, related_name='applicant_favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
