from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import ArrayField


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='applicant_user', verbose_name='Пользователь')
    response = ArrayField(models.CharField(max_length=100), verbose_name="Отклики", default=list, blank=True, null=True)
    resume_count = models.IntegerField('Счетчик резюме', default=0)

    portfolio = models.ImageField('Портфолио', null=True, blank=True, upload_to='movies/applicant_portfolio')

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатель'

    def __str__(self):
        return f"{self.user}"


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='employer_user', verbose_name='Пользователь')
    title_org = models.CharField('Название организации', blank=True, max_length=100, null=True, default='')
    photo_org = models.ImageField('Логотип', upload_to='employer', blank=True, null=True)
    inn = models.CharField('ИНН', blank=True, null=True, max_length=100, default='')
    status_valid = models.BooleanField('Статус проверки ИНН', null=True, default=False)
    job_example = models.ImageField('Достижения', upload_to='employer', blank=True, null=True)
    vacancy_count = models.IntegerField('Счетчик вакансий', default=0)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'

    def __str__(self):
        return f"{self.user}"
