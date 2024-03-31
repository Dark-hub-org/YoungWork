import uuid

from django.db import models
from accounts.models import User
from jobs.models import Vacancies
from profiles.models import Employer


class Notification(models.Model):
    type_of_notification = (
        ("VacancyResponse", 'new_vacancy_response'),
        ("AcceptedVacancy", 'accepted_vacancy_response'),
        ("RejectedVacancy", 'rejected_vacancy_response'),
        ("VacancyFavorites", 'vacancy_favorites'),
        ("PostComment", 'vacancy_comment')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    type_of_notification = models.CharField(max_length=50, choices=type_of_notification)
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_notifications', on_delete=models.CASCADE)
    created_for = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
