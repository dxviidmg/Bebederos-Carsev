# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0005_auto_20170727_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primervisita',
            name='escuela',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='primervisita',
            name='sim',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sim', to=settings.AUTH_USER_MODEL),
        ),
    ]
