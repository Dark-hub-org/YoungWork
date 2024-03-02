import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from profiles.models import Employer, Applicant


class Vacancies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=100, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    tasks = models.CharField(blank=True, null=True, default='')
    requirements = models.CharField(blank=True, null=True, default='')
    salary_min = models.BigIntegerField(blank=True, null=True, default=0)
    salary_max = models.BigIntegerField(blank=True, null=True, default=0)
    tax = models.CharField(blank=True, null=True, max_length=100, default='')
    employ = ArrayField(models.CharField(max_length=100), default=list, blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, upload_to='movies/vacancies')
    required_experience = models.CharField(blank=True, null=True, max_length=100, default='')
    graph = ArrayField(models.CharField(max_length=100), default=list, blank=False, null=False)

    favorites_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    timestamp = models.DateField(auto_now_add=False, auto_now=True)
    company_name = models.CharField(null=True, blank=True, max_length=100)
    created_by = models.ForeignKey(Employer, related_name='employer_vacancy', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансия'

    def __str__(self):
        return f"{self.job_title}"


class Response(models.Model):
    resp = (
        ("Response", 'new_response'),
        ("Invite", 'invite'),
        ("Accepted", 'accepted_response'),
        ("Rejected", 'rejected_response'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE, blank=True, null=True)
    date_start = models.DateField(auto_now_add=False, auto_now=True)
    data_end = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=50, choices=resp, default='new_vacancy_response')
    org = models.ForeignKey(Employer, related_name='employer_event', on_delete=models.CASCADE)
    created_by = models.ForeignKey(Applicant, related_name='applicant_event', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отклики'
        verbose_name_plural = 'Отклики'
