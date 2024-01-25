import datetime
import uuid

from django.db import models
from accounts.models import User
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
    graph = models.CharField(blank=True, max_length=100, default='')

    comments_count = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='vacancies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_title} {self.salary_min} {self.salary_max}"

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# TODO Forgot what is this
class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=100, default='')
    date = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.event_id)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'
