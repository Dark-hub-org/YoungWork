from django.db import models


class Applicant(models.Model):
    profile_photo = models.ImageField(upload_to='movies/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    number = models.PositiveBigIntegerField()
    tm = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    portfolio = models.ImageField(upload_to='movies/')

    def __str__(self):
        return self.first_name
