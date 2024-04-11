# Generated by Django 5.0.4 on 2024-04-10 20:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='get_contractors', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContractorUser',
        ),
    ]