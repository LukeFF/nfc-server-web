# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfctags', '0002_auto_20141219_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_capacity',
            field=models.IntegerField(help_text=b'Tag capacity in bytes', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_length',
            field=models.IntegerField(help_text=b'Message length in bytes', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_version',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
