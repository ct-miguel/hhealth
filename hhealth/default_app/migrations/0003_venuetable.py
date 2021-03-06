# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151022233823 on 2015-10-24 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_app', '0002_examinertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueTable',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, default=b'', max_length=255)),
                ('venue', models.CharField(blank=True, default=b'', max_length=255)),
                ('key', models.CharField(blank=True, default=b'', max_length=255)),
                ('description', models.CharField(blank=True, default=b'', max_length=255)),
                ('use', models.BooleanField(default=False)),
                ('capacity', models.IntegerField(default=0)),
                ('max_capacity', models.IntegerField(default=0)),
                ('start_time', models.CharField(blank=True, default=b'', max_length=255)),
            ],
        ),
    ]
