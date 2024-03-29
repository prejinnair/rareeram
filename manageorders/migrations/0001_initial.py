# Generated by Django 4.0.5 on 2022-06-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_name', models.CharField(max_length=150, null=True, unique=True)),
                ('order_date', models.CharField(max_length=70)),
                ('order_status', models.CharField(choices=[('active', 'active'), ('in-active', 'in-active'), ('delete', 'deleted')], default='active', max_length=20)),
                ('order_email', models.EmailField(max_length=200)),
                ('order_decription', models.CharField(max_length=70)),
                ('order_phone', models.CharField(max_length=150, null=True, unique=True)),
                ('order_tracking_no', models.CharField(max_length=70)),
                ('order_shipping_provider', models.CharField(max_length=100)),
                ('order_date_shipped', models.DateField(auto_now_add=True)),
                ('order_total', models.CharField(max_length=300)),
            ],
        ),
    ]
