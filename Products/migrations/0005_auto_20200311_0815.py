# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-11 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20200311_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='user_ref',
        ),
    ]