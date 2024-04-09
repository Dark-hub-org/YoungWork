from django.db import models
from jobs.models import Vacancies
from profiles.models import Employer, Applicant
import uuid


class Response(models.Model):
    resp = (
        ("Response", 'new_response'),
        ("Accepted", 'accepted_response'),
        ("Rejected", 'rejected_response'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy = models.ForeignKey(Vacancies, verbose_name="Вакансия", on_delete=models.CASCADE, blank=True, null=True)
    date_start = models.DateField('Дата создания', auto_now_add=False, auto_now=True)
    data_end = models.DateField('Дата окончания', null=True, blank=True)
    result = models.CharField('Тип отклика', max_length=50, choices=resp, default='new_vacancy_response')
    org = models.ForeignKey(Employer, verbose_name="Работодатель", related_name='employer_event',
                            on_delete=models.CASCADE)
    created_by = models.ForeignKey(Applicant, verbose_name="Откликнувшийся", related_name='applicant_event',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отклики'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f"{self.id}"
