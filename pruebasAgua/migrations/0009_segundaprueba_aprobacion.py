# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0008_auto_20170808_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='segundaprueba',
            name='aprobacion',
            field=models.CharField(choices=[('En espera', 'En espera'), ('No aprobado', 'No aprobado'), ('Aprobado', 'Aprobado')], default='En espera', max_length=11),
        ),
    ]
