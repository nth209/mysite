# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userProfileIdentity',
            field=models.IntegerField(verbose_name='S\u1ed1 ch\u1ee9ng minh nh\xe2n d\xe2n'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userProfilePermission',
            field=models.IntegerField(default=3, verbose_name='Quy\u1ec1n truy c\u1eadp'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userProfilenPhone',
            field=models.IntegerField(verbose_name='S\u1ed1 \u0111i\u1ec7n tho\u1ea1i'),
        ),
    ]
