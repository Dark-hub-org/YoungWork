# Generated by Django 4.2.2 on 2024-01-27 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_type', models.CharField(default='', max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('result', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'Событие',
            },
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('job_title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('tasks', models.CharField(blank=True, default='')),
                ('requirements', models.CharField(blank=True, default='')),
                ('salary_min', models.CharField(blank=True, default='', max_length=100)),
                ('salary_max', models.CharField(blank=True, default='', max_length=100)),
                ('tax', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(blank=True, default='', max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='movies/vacancies')),
                ('required_experience', models.CharField(blank=True, default='', max_length=100)),
                ('graph', models.CharField(blank=True, default='', max_length=100)),
                ('comments_count', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='profiles.employer')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансия',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
