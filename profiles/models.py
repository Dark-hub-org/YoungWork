from django.db import models


class Applicant(models.Model):
    sex_choice = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    )
    user_id = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='movies/applicant')
    sex = models.CharField(choices=sex_choice, default='')
    number = models.IntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.user_id)


class Employer(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='movies/employer')
    male = models.BooleanField()
    number = models.IntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.user_id)
