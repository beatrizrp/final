# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180524_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='type',
        ),
    ]
