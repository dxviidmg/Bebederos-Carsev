# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_auto_20170928_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='abreviatura',
            field=models.CharField(default='', max_length=4),
        ),
    ]
