# Generated by Django 3.0.14 on 2022-06-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Role', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='userprofile_id',
        ),
    ]
