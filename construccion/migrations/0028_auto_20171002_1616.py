# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-02 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0027_remove_evidenciaconstruccion_ejecutora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instalacionbebedero',
            name='memoria_calculo',
        ),
        migrations.RemoveField(
            model_name='instalacionbebedero',
            name='plano_instalacion',
        ),
    ]
