# Generated by Django 4.0.5 on 2022-06-14 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manageusers', '0006_rename_s_address_id_salesaddress_salesagent_address_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesagent',
            name='salesagent_address_id',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='dealers',
            old_name='dealer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='dealers',
            old_name='confirm_password',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='postalcode',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='dealer_first_name',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='dealer_gender',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='dealer_last_name',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='dealer_mobile_number',
        ),
        migrations.RemoveField(
            model_name='dealers',
            name='password',
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.EmailField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='entry_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='landmark',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='pincode',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('in-active', 'in-active'), ('delete', 'deleted')], default='in-active', max_length=20),
        ),
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('D', 'Dealer'), ('SA', 'SalesAgent')], default='D', max_length=10),
        ),
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='user_uuid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_uuid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dealers',
            name='dealer_gst_no',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dealers',
            name='dealer_image',
            field=models.ImageField(blank=True, null=True, upload_to='dealer_images'),
        ),
        migrations.AddField(
            model_name='dealers',
            name='dealer_shopname',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dealers',
            name='phone',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='area',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='dealers',
            name='address_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manageusers.address'),
        ),
        migrations.DeleteModel(
            name='SalesAddress',
        ),
        migrations.DeleteModel(
            name='SalesAgent',
        ),
    ]