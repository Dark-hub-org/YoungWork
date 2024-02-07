import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from profiles.models import Employer


class Vacancies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=100, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    tasks = models.CharField(blank=True, null=True, default='')
    requirements = models.CharField(blank=True, null=True, default='')
    salary_min = models.BigIntegerField(blank=True, null=True, default='')
    salary_max = models.BigIntegerField(blank=True, null=True, default='')
    tax = models.CharField(blank=True, null=True, max_length=100, default='')
    employ = models.CharField(blank=True, null=True, max_length=100, default='')
    logo = models.ImageField(null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField(blank=True, null=True, max_length=100, default='')
    graph = ArrayField(models.CharField(max_length=100), default=list, blank=False, null=False)

    favorites_count = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(null=True, blank=True, max_length=100)
    created_by = models.ForeignKey(Employer, related_name='employer_vacancy', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'

    def __str__(self):
        return f"{self.job_title}"


# TODO event to check inn
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(null=True, max_length=100, default='')
    date_start = models.DateTimeField(null=True, auto_now_add=True)
    data_end = models.DateTimeField(null=True, blank=True)
    result = models.CharField(null=True, max_length=100, default='')
    created_by = models.ForeignKey(Employer, related_name='employer_event', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'
