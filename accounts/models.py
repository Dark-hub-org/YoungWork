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
    avatar = models.ImageField(upload_to='movies/avatars', null=True)

    recommendations = models.ManyToManyField('self')

    vacancy_count = models.IntegerField(default=0)
    resume_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(blank=True, null=True, max_length=100, default='')
    last_name = models.CharField(blank=True, null=True, max_length=100, default='')
    surname = models.CharField(blank=True, null=True, max_length=100, default='')
    date_of_birth = models.CharField(blank=True, null=True, default='')
    citizenship = models.CharField(blank=True, null=True, max_length=50, default='')
    region = models.CharField(blank=True, null=True, max_length=50, default='')
    city = models.CharField(blank=True, null=True, max_length=50, default='')
    about = models.CharField(blank=True, null=True, default='')
    about_work = models.CharField(blank=True, null=True, default='')
    telegram = models.CharField(blank=True, null=True, max_length=100, default='')
    website = models.CharField(blank=True, null=True, max_length=100, default='')
    phone_number = models.CharField(blank=True, null=True, max_length=100, default='')

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["usertype"]

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return 'https://picsum.photos/200/200'

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


class VacancyResponse(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (SENT, 'Sent'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(User, related_name='received_vacancy_response', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='created_vacancy_response', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)
