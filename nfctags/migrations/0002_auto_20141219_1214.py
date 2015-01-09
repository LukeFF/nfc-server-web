# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfctags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfctag',
            name='reader',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='memdump',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_capacity',
            field=models.IntegerField(verbose_name=b'in bytes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_length',
            field=models.IntegerField(verbose_name=b'in bytes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='ndef_message',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tagtype',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
