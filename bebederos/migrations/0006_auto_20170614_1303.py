# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0005_auto_20170614_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sistemabebedero',
            old_name='bebedero',
            new_name='mueble',
        ),
    ]
