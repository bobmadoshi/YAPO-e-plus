# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-02-22 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0037_auto_20180722_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='piercings',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='hash',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
	]
