# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0008_virtualmachine_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualMachineHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
            ],
        ),
    ]
