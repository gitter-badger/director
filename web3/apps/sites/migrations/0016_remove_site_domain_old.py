# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-29 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0015_auto_20170429_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='domain_old',
        ),
    ]
