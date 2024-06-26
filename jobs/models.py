import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from profiles.models import Employer


class Vacancies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField('Название организации', max_length=100, null=True, default='')
    description = models.TextField('Описание', blank=True, null=True, default='')
    tasks = models.CharField('Задачи', blank=True, null=True, default='')
    requirements = models.CharField('Требования', blank=True, null=True, default='')
    salary_min = models.BigIntegerField('Минемальная зарплата', blank=True, null=True, default=0)
    salary_max = models.BigIntegerField('Максимальная зарплата', blank=True, null=True, default=0)
    tax = models.CharField('Статус налога', blank=True, null=True, max_length=100, default='')
    employ = ArrayField(models.CharField(max_length=100), verbose_name="Тип занятости", default=list, blank=True,
                        null=True)
    banner = models.ImageField('Баннер', null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField('Требуемый опыт', blank=True, null=True, max_length=100, default='')
    graph = ArrayField(models.CharField('График', max_length=100), default=list, blank=False, null=False)

    favorites_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    timestamp = models.DateField('Дата создания', auto_now_add=False, auto_now=True)
    company_name = models.CharField('Название организации', null=True, blank=True, max_length=100)
    created_by = models.ForeignKey(Employer, verbose_name="Создатель", related_name='employer_vacancy',
                                   on_delete=models.CASCADE)

    com_logo = models.CharField('Фото компании', null=True, blank=True)
    citizenship = models.CharField('Страна', blank=True, null=True, max_length=50, default='')
    region = models.CharField('Регион', blank=True, null=True, max_length=50, default='')
    city = models.CharField('Город', blank=True, null=True, max_length=50, default='')
    phone_number = models.CharField('Номер телефона', blank=True, null=True, max_length=100, default='')
    first_name = models.CharField('Имя', blank=True, null=True, max_length=100, default='')
    last_name = models.CharField('Фамилия', blank=True, null=True, max_length=100, default='')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'

    def __str__(self):
        return f"{self.job_title}"
