# Generated by Django 4.2.2 on 2024-01-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dampuser',
            name='birthday',
            field=models.DateField(blank=True, default='1999-01-01'),
        ),
        migrations.AlterField(
            model_name='dampuser',
            name='citizenship',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dampuser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dampuser',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='dampuser',
            name='region',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]