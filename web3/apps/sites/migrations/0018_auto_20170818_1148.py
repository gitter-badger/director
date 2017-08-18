# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0017_auto_20170707_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('port', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('dbms', models.CharField(choices=[('postgresql', 'PostgreSQL'), ('mysql', 'MySQL')], max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='database',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.DatabaseHost'),
        ),
    ]
