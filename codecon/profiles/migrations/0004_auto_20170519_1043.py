# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170519_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.FileField(blank=True, upload_to='profile_photos/%Y/%m/%d/'),
        ),
    ]
