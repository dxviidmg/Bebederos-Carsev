# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-17 23:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0035_auto_20171105_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iniciodetrabajo',
            name='escuela',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='escuela_inicio_trabajo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='escuela',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='escuela_instalacion_bebedero', to=settings.AUTH_USER_MODEL),
        ),
    ]
