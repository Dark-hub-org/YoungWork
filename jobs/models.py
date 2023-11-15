from django.db import models
from django.contrib.auth.models import User
from profiles.models import Employer


class Vacancies(models.Model):
    type_choice = (
        ('full', 'Полная'),
        ('partial', 'Частичная'),
        ('internship', 'Стажировка'),
        ('volunteering', 'Волонтерство'),
    )
    tax_choice = (
        ('before', 'До вычета налогов'),
        ('after', 'На руки')
    )
    required_experience = (
        ('nothing', 'Без опыта'),
        ('1to3', 'от 1 года до 3 лет'),
        ('3to6', 'от 3 до 6 лут'),
        ('6up', 'Более 6 лет'),
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                   related_name='vacancies_user')
    job_title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    salary_min = models.CharField(max_length=100, default='')
    salary_max = models.CharField(max_length=100, default='')
    tax = models.CharField(choices=tax_choice, default='')
    type = models.CharField(choices=type_choice, default='')
    logo = models.ImageField(null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField(choices=required_experience, default='')
    requirements = models.CharField(max_length=100, default='')
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'


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
