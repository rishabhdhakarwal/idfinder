# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
