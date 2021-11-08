# Generated by Django 3.2.9 on 2021-11-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('did', models.UUIDField(primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.IntegerField(max_length=255)),
                ('education', models.TextField()),
                ('qualification', models.TextField()),
                ('specialty', models.TextField()),
                ('experience', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('rmp', models.CharField(max_length=255)),
            ],
        ),
    ]