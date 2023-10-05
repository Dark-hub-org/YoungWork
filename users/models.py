from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name_1 = models.TextField(max_length=55, default='')
    last_name_1 = models.TextField(max_length=55, default='')
    short_name = models.TextField(max_length=55, default='')
