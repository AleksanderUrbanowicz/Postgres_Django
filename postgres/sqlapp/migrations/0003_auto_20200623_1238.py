# Generated by Django 3.0.7 on 2020-06-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0002_transaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]
