# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160212_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='update_time',
        ),
    ]
