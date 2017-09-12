# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bebederos', '0019_auto_20170829_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistemabebedero',
            name='constructora',
        ),
        migrations.AddField(
            model_name='sistemabebedero',
            name='ejecutora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ejecutora', to=settings.AUTH_USER_MODEL),
        ),
    ]
