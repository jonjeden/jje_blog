# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-10 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161109_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Project'),
        ),
    ]