# Generated by Django 5.0.6 on 2024-08-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankaccount',
            name='phone',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='country',
            field=models.CharField(default='USA', max_length=100),
        ),
    ]
