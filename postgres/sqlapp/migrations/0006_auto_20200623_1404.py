# Generated by Django 3.0.7 on 2020-06-23 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0005_auto_20200623_1402'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productcategory',
            table='categories',
        ),
    ]
