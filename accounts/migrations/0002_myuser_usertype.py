# Generated by Django 5.0.1 on 2024-01-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='usertype',
            field=models.CharField(blank=True, default=''),
        ),
    ]
