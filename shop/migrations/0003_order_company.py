# Generated by Django 5.0.4 on 2024-04-11 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contractor_user_delete_contractoruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.contractor', verbose_name='Организация покупателя'),
        ),
    ]