# Generated by Django 4.0.4 on 2022-06-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0002_dealers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealers',
            name='dealer_status',
            field=models.CharField(choices=[('active', 'active'), ('in-active', 'in-active'), ('delete', 'deleted')], default='active', max_length=20),
        ),
    ]
