# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-06 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluators', '0002_auto_20161206_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluator',
            old_name='types',
            new_name='evaltypes',
        ),
    ]
