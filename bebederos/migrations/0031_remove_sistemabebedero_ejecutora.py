# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0030_auto_20170929_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistemabebedero',
            name='ejecutora',
        ),
    ]
