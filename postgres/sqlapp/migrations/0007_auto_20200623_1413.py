# Generated by Django 3.0.7 on 2020-06-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0006_auto_20200623_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
