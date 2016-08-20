# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 06:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.URLField(default='https://lh4.googleusercontent.com/-fEed_duHZ0E/VpPTyoNjdGI/AAAAAAAADNE/by47Xe84u2g4_dzc9ixG_V7gKF5Ep_C6gCL0B/w854-h852-no/maxresdefault.jpg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userp.UserProfile'),
        ),
    ]
