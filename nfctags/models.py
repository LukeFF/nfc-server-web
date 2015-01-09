from django.db import models

class NfcTag(models.Model):
    uid = models.CharField(max_length=200)
    tagtype = models.ForeignKey('TagType')
    sak = models.CharField(max_length=200, null=True)
    atq = models.CharField(max_length=200, null=True)
    timestamp = models.DateTimeField('time scanned')
    reader = models.CharField(max_length=200, null=True)
    ndef_version = models.CharField(max_length=200, null=True, blank=True)
    ndef_readable = models.NullBooleanField()
    ndef_writeable = models.NullBooleanField()
    ndef_capacity = models.IntegerField(null=True, blank=True, help_text='Tag capacity in bytes')
    ndef_length = models.IntegerField(null=True, blank=True, help_text='Message length in bytes')
    ndef_message = models.TextField(blank=True)

    def __unicode__(self):
        return self.uid

class TagType(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)
    access = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
