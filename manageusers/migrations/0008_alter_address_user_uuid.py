# Generated by Django 4.0.5 on 2022-06-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0007_remove_salesagent_salesagent_address_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user_uuid',
            field=models.CharField(default='', max_length=100),
        ),
    ]