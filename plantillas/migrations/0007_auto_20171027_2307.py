# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-28 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantillas', '0006_auto_20171018_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='archivo',
            field=models.FileField(upload_to='plantillas/%Y/%m/%d/'),
        ),
    ]
