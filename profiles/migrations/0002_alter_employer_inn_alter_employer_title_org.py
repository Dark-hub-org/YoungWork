# Generated by Django 4.2.2 on 2024-01-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='inn',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employer',
            name='title_org',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
