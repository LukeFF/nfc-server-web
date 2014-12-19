# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NfcTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=200)),
                ('ndef_version', models.CharField(max_length=200)),
                ('ndef_readable', models.NullBooleanField()),
                ('ndef_writeable', models.NullBooleanField()),
                ('ndef_capacity', models.IntegerField()),
                ('ndef_length', models.IntegerField()),
                ('ndef_message', models.TextField()),
                ('memdump', models.TextField()),
                ('timestamp', models.DateTimeField(verbose_name=b'time scanned')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=200)),
                ('speed', models.CharField(max_length=200)),
                ('access', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nfctag',
            name='tagtype',
            field=models.ForeignKey(to='nfctags.TagType'),
            preserve_default=True,
        ),
    ]
