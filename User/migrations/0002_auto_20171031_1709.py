# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='user_pwd',
            field=models.CharField(max_length=100),
        ),
    ]
