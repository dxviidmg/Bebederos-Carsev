# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0015_auto_20170822_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='notadebitacora',
            name='resuelto',
            field=models.BooleanField(default=False),
        ),
    ]
