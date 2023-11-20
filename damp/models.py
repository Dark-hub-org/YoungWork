from django.db import models
from django.contrib.auth.models import User


class DampUser(models.Model):
    gender = {
        ('Мужской', 0),
        ('Женский', 1)
    }
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                   related_name='user')
    photo = models.ImageField(default='')
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=20, default='')
    gender = models.CharField(choices=gender, default='')
    birthday = models.DateField(default='2009-02-11')
    citizenship = models.CharField(max_length=20, default='')
    region = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
