# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfctags', '0004_auto_20141219_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfctag',
            name='memdump',
        ),
        migrations.AddField(
            model_name='nfctag',
            name='atq',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nfctag',
            name='sak',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
