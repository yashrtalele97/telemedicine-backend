# Generated by Django 3.2.9 on 2021-11-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20211105_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]