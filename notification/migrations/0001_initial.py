# Generated by Django 4.2.2 on 2024-04-13 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('type_of_notification', models.CharField(choices=[('VacancyResponse', 'new_vacancy_response'), ('AcceptedVacancy', 'accepted_vacancy_response'), ('RejectedVacancy', 'rejected_vacancy_response'), ('VacancyFavorites', 'vacancy_favorites'), ('ResumeFavorites', 'resume_favorites')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_notifications', to=settings.AUTH_USER_MODEL)),
                ('created_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL)),
                ('resume', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
                ('vacancy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.vacancies')),
                ('vacancyresponse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='response.response')),
            ],
        ),
    ]
