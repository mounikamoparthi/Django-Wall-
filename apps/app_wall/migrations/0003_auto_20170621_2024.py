# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_wall', '0002_auto_20170621_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg', to='app_wall.Message'),
        ),
    ]
