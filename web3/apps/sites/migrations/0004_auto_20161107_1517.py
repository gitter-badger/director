# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20161105_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField(path='/web')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='custom_nginx',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='site',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Group'),
        ),
        migrations.AlterField(
            model_name='site',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='process',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
