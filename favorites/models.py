from django.db import models
from resume.models import Resume
from jobs.models import Vacancies
import uuid
from accounts.models import User


class Favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume = models.ManyToManyField(Resume, verbose_name="Резюме", related_name='resume', null=True, blank=True)
    vacancy = models.ManyToManyField(Vacancies, verbose_name="Вакансия", related_name='vacancies', null=True,
                                     blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name="Создатель", related_name='user_favorites',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f"{self.id}"
