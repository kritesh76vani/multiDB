# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-11 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_remove_product_user_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='db',
        ),
    ]