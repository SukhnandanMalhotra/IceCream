# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0026_auto_20160901_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.RemoveField(
            model_name='registration',
            name='designer',
        ),
    ]