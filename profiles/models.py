from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):
    sex_choice = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='applicant_releted_user')
    bio = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='movies/applicant')
    sex = models.CharField(choices=sex_choice, default='')
    number = models.IntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Employer(models.Model):
    sex_choice = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                related_name='employee_releted_user')
    about_us = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='movies/employer')
    sex = models.CharField(choices=sex_choice, default='')
    inn = models.CharField(max_length=50, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
