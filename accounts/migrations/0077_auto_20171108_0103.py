# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-08 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0076_auto_20171107_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='partida',
            field=models.IntegerField(verbose_name='Partida'),
        ),
        migrations.AlterField(
            model_name='region',
            name='color',
            field=models.CharField(max_length=10, verbose_name='Color (Hexadecimal o en inglés)'),
        ),
        migrations.AlterField(
            model_name='zona',
            name='color',
            field=models.CharField(max_length=30, verbose_name='Color (Hexadecimal o en inglés)'),
        ),
    ]
