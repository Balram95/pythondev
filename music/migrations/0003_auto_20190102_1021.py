# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-02 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_releasedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='detailis',
            new_name='details',
        ),
    ]
