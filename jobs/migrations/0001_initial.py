# Generated by Django 4.2.2 on 2024-01-02 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='event_user', serialize=False, to=settings.AUTH_USER_MODEL)),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('salary_min', models.CharField(default='', max_length=100)),
                ('salary_max', models.CharField(default='', max_length=100)),
                ('tax', models.CharField(choices=[('before', 'До вычета налогов'), ('after', 'На руки')], default='')),
                ('type', models.CharField(choices=[('full', 'Полная'), ('partial', 'Частичная'), ('internship', 'Стажировка'), ('volunteering', 'Волонтерство')], default='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='movies/vacancies')),
                ('required_experience', models.CharField(choices=[('nothing', 'Без опыта'), ('1to3', 'от 1 года до 3 лет'), ('3to6', 'от 3 до 6 лут'), ('6up', 'Более 6 лет')], default='')),
                ('requirements', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансия',
            },
        ),
    ]
