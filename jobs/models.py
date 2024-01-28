import uuid

from django.db import models
from profiles.models import Employer


class Vacancies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, default='')
    tasks = models.CharField(blank=True, default='')
    requirements = models.CharField(blank=True, default='')
    salary_min = models.CharField(blank=True, max_length=100, default='')
    salary_max = models.CharField(blank=True, max_length=100, default='')
    tax = models.CharField(blank=True, max_length=100, default='')
    type = models.CharField(blank=True, max_length=100, default='')
    logo = models.ImageField(null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField(blank=True, max_length=100, default='')
    graph = models.CharField(blank=True, default='')

    favorites_count = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employer, related_name='employer_vacancy', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'


# TODO event to check inn
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=100, default='')
    date_start = models.DateTimeField(auto_now_add=True)
    data_end = models.DateTimeField(null=True, blank=True)
    result = models.CharField(max_length=100, default='')
    created_by = models.ForeignKey(Employer, related_name='employer_event', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'
