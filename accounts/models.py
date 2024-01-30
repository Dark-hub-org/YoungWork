import uuid

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, usertype, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            usertype=usertype,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, usertype, password=None):
        user = self.create_user(
            email,
            password=password,
            usertype=usertype,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    usertype = models.CharField()
    avatar = models.ImageField(upload_to='movies/avatars', blank=True, null=True)

    recommendations = models.ManyToManyField('self')

    posts_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(blank=True, max_length=100, default='')
    last_name = models.CharField(blank=True, max_length=100, default='')
    surname = models.CharField(blank=True, max_length=100, default='')
    date_of_birth = models.DateField(default='0001-01-01', blank=True, null=True)
    citizenship = models.CharField(blank=True, max_length=50, default='')
    region = models.CharField(blank=True, max_length=50, default='')
    city = models.CharField(blank=True, max_length=50, default='')
    gender = models.CharField(blank=True, default='')
    about = models.CharField(blank=True, default='')
    about_work = models.CharField(blank=True, default='')
    telegram = models.CharField(blank=True, max_length=100, default='')
    website = models.CharField(blank=True, max_length=100, default='')
    phone_number = models.CharField(blank=True, max_length=100, default='')

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["usertype"]

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return 'https://github.com/Dark-hub-org/YoungWork/blob/83981ff8000cebb6f3c0602f5f4e7bcc55c3e8db/frontend/src/assets/header/anonim-logo.svg'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователь'
