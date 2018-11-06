# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-06 04:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('link', '0005_delete_slink'),
    ]

    operations = [
        migrations.CreateModel(
            name='slink',
            fields=[
                ('LinkID', models.AutoField(primary_key=True, serialize=False)),
                ('LinkName', models.CharField(blank=True, max_length=2000, null=True, verbose_name='T\xean \u0111\u1ec3 nh\u1edb')),
                ('LinkURL', models.TextField(max_length=2000, verbose_name='Link')),
                ('LinkDate', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Ng\xe0y luu')),
                ('LinkDescription', models.TextField(blank=True, max_length=2000, null=True, verbose_name='L\u01b0u \xfd')),
            ],
        ),
    ]
