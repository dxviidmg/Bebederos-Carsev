# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_entidad_abreviatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='abreviatura',
            field=models.CharField(max_length=4),
        ),
    ]
