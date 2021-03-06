# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-22 02:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0036_folder_path_with_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 3, 664233)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actoralias',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 22, 2, 18, 19, 87551)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actortag',
            name='actor_tag_alias',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='actortag',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 27, 500673)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actortag',
            name='scene_tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='actor_tags', to='videos.SceneTag'),
        ),
        migrations.AddField(
            model_name='folder',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 22, 2, 18, 36, 398786)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 41, 152903)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localscenefolders',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 7, 22, 2, 18, 46, 305888)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scene',
            name='date_last_played',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='last_filename_tag_lookup',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 51, 185019)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenetag',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 55, 404441)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scenetag',
            name='scene_tag_alias',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='website',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 7, 22, 2, 18, 59, 247075)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website',
            name='website_alias',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='playlist',
            name='scenes',
            field=models.ManyToManyField(blank=True, null=True, related_name='playlists', to='videos.Scene'),
        ),
    ]
