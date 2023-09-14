# Generated by Django 4.2.2 on 2023-09-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='movies/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateTimeField()),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('number', models.PositiveBigIntegerField()),
                ('tm', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('portfolio', models.ImageField(upload_to='movies/')),
            ],
        ),
    ]
