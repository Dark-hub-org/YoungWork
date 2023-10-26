from django.db import models
from profiles.models import Applicant


class Summary(models.Model):
    experience = (
        ('nothing', 'Без опыта'),
        ('1to3', 'от 1 года до 3 лет'),
        ('3to6', 'от 3 до 6 лут'),
        ('6up', 'Более 6 лет'),
    )
    type_choice = (
        ('full', 'Полная'),
        ('partial', 'Частичная'),
        ('internship', 'Стажировка'),
        ('volunteering', 'Волонтерство'),
    )
    summary_title = models.CharField(max_length=100, default='')
    type = models.CharField(choices=type_choice, default='')
    about_us = models.TextField(max_length=55, default='')
    experience = models.CharField(choices=experience, default='')
    skills = models.CharField(max_length=100, default='')
    quality = models.CharField(max_length=100, default='')
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE, default='')

    def __str__(self):
        return str(self.summary_title)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
