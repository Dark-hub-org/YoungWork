# Generated by Django 4.2.2 on 2024-02-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]
