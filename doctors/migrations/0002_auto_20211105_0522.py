# Generated by Django 3.2.9 on 2021-11-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='phone',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='rmp',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
