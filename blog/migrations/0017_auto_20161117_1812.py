# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-18 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20161116_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='Required', max_length=40),
        ),
    ]
