from django.db import models


class Vacancy(models.Model):
    poster = models.ImageField(upload_to='movies/')
    title = models.CharField(max_length=100)
    salary_min = models.PositiveSmallIntegerField(default=0)
    salary_max = models.PositiveSmallIntegerField(default=0)
    company = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)
    require = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
