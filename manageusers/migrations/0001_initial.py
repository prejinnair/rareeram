# Generated by Django 4.0.4 on 2022-06-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=150, null=True, unique=True)),
                ('area', models.CharField(max_length=150, null=True, unique=True)),
                ('country', models.CharField(max_length=150, null=True, unique=True)),
                ('postalcode', models.CharField(max_length=150, null=True, unique=True)),
            ],
        ),
    ]
