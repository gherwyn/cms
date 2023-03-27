# Generated by Django 4.1.7 on 2023-03-26 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, verbose_name='firstname')),
                ('user_lname', models.CharField(max_length=200, verbose_name='lastname')),
                ('user_email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('user_position', models.CharField(max_length=200, verbose_name='position')),
                ('pub_date', models.DateField(default=datetime.datetime(2023, 3, 26, 5, 51, 7, 219278, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
