# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-27 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0042_auto_20171206_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iniciodetrabajo',
            name='acta_inicio',
            field=models.FileField(upload_to='iniciosTrabajo/actas/%Y/%m/%d/', verbose_name='Acta de inicio de construcción'),
        ),
    ]
