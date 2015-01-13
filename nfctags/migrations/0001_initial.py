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
                ('sak', models.CharField(max_length=200, null=True)),
                ('atq', models.CharField(max_length=200, null=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'time scanned')),
                ('reader', models.CharField(max_length=200, null=True)),
                ('ndef_version', models.CharField(max_length=200, null=True, blank=True)),
                ('ndef_readable', models.NullBooleanField()),
                ('ndef_writeable', models.NullBooleanField()),
                ('ndef_capacity', models.IntegerField(help_text=b'Tag capacity in bytes', null=True, blank=True)),
                ('ndef_length', models.IntegerField(help_text=b'Message length in bytes', null=True, blank=True)),
                ('ndef_message', models.TextField(blank=True)),
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
                ('description', models.TextField(blank=True)),
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
