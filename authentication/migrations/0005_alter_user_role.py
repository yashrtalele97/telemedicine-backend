# Generated by Django 3.2.9 on 2022-05-15 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
