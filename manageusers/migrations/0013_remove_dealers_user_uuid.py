# Generated by Django 4.0.5 on 2022-06-16 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0012_alter_dealers_user_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealers',
            name='user_uuid',
        ),
    ]