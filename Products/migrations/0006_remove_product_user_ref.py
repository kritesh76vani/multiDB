# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-11 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_auto_20200311_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_ref',
        ),
    ]
