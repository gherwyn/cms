# Generated by Django 4.1.7 on 2023-03-26 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsmain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='user_name',
            new_name='user_fname',
        ),
        migrations.AlterField(
            model_name='projects',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 26, 5, 54, 20, 856079, tzinfo=datetime.timezone.utc)),
        ),
    ]