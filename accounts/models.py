from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
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


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    usertype = models.CharField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    photo = models.ImageField(blank=True, default='')
    first_name = models.CharField(blank=True, max_length=20, default='')
    last_name = models.CharField(blank=True, max_length=20, default='')
    surname = models.CharField(blank=True, max_length=20, default='')
    date_of_birth = models.DateField(blank=True, default='1999-01-01')
    citizenship = models.CharField(blank=True, max_length=20, default='')
    region = models.CharField(blank=True, max_length=20, default='')
    city = models.CharField(blank=True, max_length=20, default='')
    send_email = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["usertype"]

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