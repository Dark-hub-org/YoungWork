from django.db import models
from accounts.models import MyUser


class Applicant(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True,
                                related_name='applicant_user')
    bio = models.TextField(null=True, blank=True)
    portfolio = models.ImageField(null=True, blank=True, upload_to='movies/applicant_portfolio')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатель'


class Employer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True,
                                related_name='employer_releted_user')
    inn = models.CharField(max_length=100)
    title_org = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo_org = models.ImageField(null=True, blank=True, upload_to='movies/employer')
    job_title = models.CharField(max_length=100)
    status_validatio = models.CharField(max_length=100)
    job_example = models.ImageField(null=True, blank=True, upload_to='movies/employer')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'
