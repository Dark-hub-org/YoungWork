# Generated by Django 5.0.1 on 2024-01-27 17:16

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('usertype', models.CharField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='movies/avatars')),
                ('posts_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, default='', max_length=20)),
                ('last_name', models.CharField(blank=True, default='', max_length=20)),
                ('surname', models.CharField(blank=True, default='', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, default='1999-01-01')),
                ('citizenship', models.CharField(blank=True, default='', max_length=20)),
                ('region', models.CharField(blank=True, default='', max_length=20)),
                ('city', models.CharField(blank=True, default='', max_length=20)),
                ('bio', models.TextField(blank=True, default='')),
                ('portfolio', models.ImageField(blank=True, null=True, upload_to='movies/applicant_portfolio')),
                ('recommendations', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Соискатель',
                'verbose_name_plural': 'Соискатель',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('usertype', models.CharField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='movies/avatars')),
                ('posts_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, default='', max_length=20)),
                ('last_name', models.CharField(blank=True, default='', max_length=20)),
                ('surname', models.CharField(blank=True, default='', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, default='1999-01-01')),
                ('citizenship', models.CharField(blank=True, default='', max_length=20)),
                ('region', models.CharField(blank=True, default='', max_length=20)),
                ('city', models.CharField(blank=True, default='', max_length=20)),
                ('title_org', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo_org', models.ImageField(blank=True, null=True, upload_to='movies/employer')),
                ('inn', models.CharField(blank=True, max_length=100)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('status_valid', models.CharField(blank=True, max_length=100)),
                ('job_example', models.ImageField(blank=True, null=True, upload_to='movies/employer')),
                ('recommendations', models.ManyToManyField(to='accounts.employer')),
            ],
            options={
                'verbose_name': 'Работадатель',
                'verbose_name_plural': 'Работадатель',
            },
        ),
    ]
