# Generated by Django 4.0.5 on 2022-06-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0008_alter_address_user_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='email',
        ),
    ]
