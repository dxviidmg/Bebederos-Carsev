# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0003_auto_20170614_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistemabebedero',
            name='mueble',
        ),
        migrations.DeleteModel(
            name='Mueble',
        ),
    ]
