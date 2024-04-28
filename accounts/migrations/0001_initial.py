# Generated by Django 4.2.2 on 2024-04-13 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Почта')),
                ('usertype', models.CharField(help_text='Пример: employer/applicant', verbose_name='Тип пользователя')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Фото профиля')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Фамилия')),
                ('surname', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.CharField(blank=True, default='', help_text='Пример: 1999-10-12', null=True, verbose_name='Дата рождения')),
                ('citizenship', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Страна')),
                ('region', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Регион')),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Город')),
                ('about', models.CharField(blank=True, default='', null=True, verbose_name='О вас')),
                ('about_work', models.CharField(blank=True, default='', null=True, verbose_name='Портфолио')),
                ('telegram', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Телеграм')),
                ('website', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Сайт')),
                ('phone_number', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
            },
        ),
    ]
