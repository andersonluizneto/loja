# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-27 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
