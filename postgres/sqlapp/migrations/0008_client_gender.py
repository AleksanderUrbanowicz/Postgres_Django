# Generated by Django 3.0.7 on 2020-06-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0007_auto_20200623_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')], default='U', max_length=1),
        ),
    ]
