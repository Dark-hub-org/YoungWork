from django.db import models
from accounts.models import User
from django.contrib.postgres.fields import ArrayField


class Applicant_image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='image_applicant_user', verbose_name='Пользователь')
    applicant_image = models.ImageField("Фото", null=True, blank=True, upload_to='applicant/portfolio')


class Employer_image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='image_employer_user', verbose_name='Пользователь')
    employer_image = models.ImageField("Фото", null=True, blank=True, upload_to='employer/achievements')

    def __str__(self):
        return f"{self.employer_image}"


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='applicant_user', verbose_name='Пользователь')
    response = ArrayField(models.CharField(max_length=100), verbose_name="Отклики", default=list, blank=True, null=True)
    resume_count = models.IntegerField('Счетчик резюме', default=0)

    portfolio = models.ManyToManyField(Applicant_image, related_name='portfolio', verbose_name='Портфолио', blank=True)

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
    achievements = models.ManyToManyField(Employer_image, related_name='achievements', verbose_name='Достижения', blank=True)
    vacancy_count = models.IntegerField('Счетчик вакансий', default=0)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатель'

    def __str__(self):
        return f"{self.user}"
