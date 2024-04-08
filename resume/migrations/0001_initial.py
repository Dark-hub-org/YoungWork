# Generated by Django 4.2.2 on 2024-04-07 11:47

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('resume_title', models.CharField(default='', max_length=100, null=True, verbose_name='Название')),
                ('salary', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='Зарплата')),
                ('employ', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, null=True, size=None, verbose_name='Тип занятости')),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, verbose_name='Навыки'), blank=True, default=list, null=True, size=None, verbose_name='Навыки')),
                ('quality', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, null=True, size=None, verbose_name='Качества')),
                ('experience', models.CharField(blank=True, default='', null=True, verbose_name='Опыт')),
                ('about_us', models.TextField(blank=True, default='', null=True, verbose_name='О вам')),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateField(auto_now=True, verbose_name='Дата вызова')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_resume', to='profiles.applicant', verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('vacancy', models.ManyToManyField(related_name='vacancies', to='jobs.vacancies', verbose_name='Вакансия')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
    ]
