# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_photo',
            field=models.FileField(upload_to='cover_photo_uploads/%Y/%m/%d/'),
        ),
    ]