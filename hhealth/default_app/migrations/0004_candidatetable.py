# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151022233823 on 2015-10-24 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default_app', '0003_venuetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateTable',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, default=b'', max_length=255)),
                ('lastname', models.CharField(blank=True, default=b'', max_length=255)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='default_app.VenueTable')),
            ],
        ),
    ]