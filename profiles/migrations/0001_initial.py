# Generated by Django 4.2.2 on 2023-10-03 21:20

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
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='movies/applicant')),
                ('male', models.BooleanField()),
                ('number', models.IntegerField(blank=True, null=True)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('web', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='movies/employer')),
                ('male', models.BooleanField()),
                ('number', models.IntegerField(blank=True, null=True)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('web', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
