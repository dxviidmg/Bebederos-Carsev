# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0017_auto_20170729_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mueble',
            old_name='cantidad_boquillas',
            new_name='cantidad_salidas_discapacidad',
        ),
        migrations.RenameField(
            model_name='mueble',
            old_name='cantidad_boquillas_discapacidad',
            new_name='cantidad_salidas_regulares',
        ),
    ]
