from django.db import models
from accounts.models import User


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='applicant_user')
    views = models.IntegerField(default=0)
    portfolio = models.ImageField(null=True, blank=True, upload_to='movies/applicant_portfolio')

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатель'

    def __str__(self):
        return f"{self.user}"


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='employer_user')
    title_org = models.CharField(blank=True, max_length=100, null=True, default='')
    photo_org = models.ImageField(null=True, blank=True, upload_to='movies/employer')
    inn = models.CharField(blank=True, null=True, max_length=100, default='')
    status_valid = models.BooleanField(null=True, default=False)
    job_example = models.ImageField(null=True, blank=True, upload_to='movies/employer')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчик'

    def __str__(self):
        return f"{self.user}"
