# Generated by Django 5.1.4 on 2025-01-18 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_remove_tenant_lease_details_tenant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='password',
            field=models.CharField(default='123', max_length=255),
        ),
        migrations.AddField(
            model_name='tenant',
            name='username',
            field=models.CharField(default='Tenant', max_length=255),
        ),
        migrations.DeleteModel(
            name='PropertyTenant',
        ),
    ]
