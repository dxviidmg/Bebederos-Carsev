# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-17 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0091_año'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Año',
            new_name='Anio',
        ),
        migrations.RenameField(
            model_name='anio',
            old_name='año',
            new_name='anio',
        ),
    ]
