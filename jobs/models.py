import datetime
from django.db import models
from django.contrib.auth.models import User
from profiles.models import Employer


class Vacancies(models.Model):
    job_title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, default='')
    salary_min = models.CharField(blank=True, max_length=100, default='')
    salary_max = models.CharField(blank=True, max_length=100, default='')
    tax = models.CharField(blank=True, max_length=100, default='')
    type = models.CharField(blank=True, max_length=100, default='')
    logo = models.ImageField(null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField(blank=True, max_length=100, default='')
    graph = models.CharField(blank=True, max_length=100, default='')

    def __str__(self):
        return f"{self.job_title} {self.salary_min} {self.salary_max}"

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'


# TODO Forgot what is this
class Events(models.Model):
    event_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                    related_name='event_user')
    event_type = models.CharField(max_length=100, default='')
    date = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.event_id)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'Событие'
