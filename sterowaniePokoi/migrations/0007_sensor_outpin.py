# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sterowaniePokoi', '0006_sensor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='outPin',
            field=models.IntegerField(default=-1),
        ),
    ]
