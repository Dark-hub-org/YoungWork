from django.db import models
from django.contrib.auth.models import User


class DampUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,
                                   related_name='user')
    photo = models.ImageField(blank=True, default='')
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    surname = models.CharField(max_length=20, default='')
    birthday = models.DateField(blank=True, default='1999-01-01')
    citizenship = models.CharField(blank=True, max_length=20, default='')
    region = models.CharField(blank=True, max_length=20, default='')
    city = models.CharField(blank=True, max_length=20, default='')

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
