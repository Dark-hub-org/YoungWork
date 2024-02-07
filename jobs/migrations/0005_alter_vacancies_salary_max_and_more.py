# Generated by Django 4.2.2 on 2024-02-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_vacancies_salary_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='salary_max',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='salary_min',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
