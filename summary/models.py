from django.db import models
from profiles.models import Applicant


class Summary(models.Model):
    experience = (
        ('noExp', 'Без опыта'),
        ('1-3', 'от 1 года до 3 лет'),
        ('3-6', 'от 3 до 6 лут'),
    )
    summary_title = models.CharField(max_length=100, default='')
    type = models.CharField(blank=True, default='')
    skills = models.CharField(blank=True, max_length=100, default='')
    quality = models.CharField(blank=True, max_length=100, default='')
    experience = models.CharField(blank=True, choices=experience, default='')
    about_us = models.TextField(blank=True, default='')
    phone_number = models.CharField(blank=True, max_length=100, default='')
    email = models.EmailField(blank=True, max_length=100, default='')
    tm = models.CharField(blank=True, max_length=100, default='')
    website = models.URLField(blank=True)

    def __str__(self):
        return str(self.summary_title)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
