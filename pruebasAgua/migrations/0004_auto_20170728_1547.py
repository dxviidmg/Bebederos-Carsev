# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0003_auto_20170727_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primerprueba',
            old_name='constancia_de_recepcion',
            new_name='constancia_recepcion',
        ),
        migrations.RenameField(
            model_name='segundaprueba',
            old_name='constancia_de_recepcion',
            new_name='constancia_recepcion',
        ),
    ]
