# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-22 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0092_auto_20180522_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segundaprueba',
            name='dictamen_validacion',
        ),
        migrations.AddField(
            model_name='segundaprueba',
            name='dictamen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pruebasAgua.DictamenIMTA'),
        ),
    ]
