# Generated by Django 3.0.7 on 2020-06-23 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
