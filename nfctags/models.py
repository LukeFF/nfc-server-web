from django.db import models

# Create your models here.
class NfcTag(models.Model):
    uid = models.CharField(max_length=200)
    tagtype = models.ForeignKey('TagType')
    ndef_version = models.CharField(max_length=200)
    ndef_readable = models.NullBooleanField()
    ndef_writeable = models.NullBooleanField()
    ndef_capacity = models.IntegerField('in bytes')
    ndef_length = models.IntegerField('in bytes')
    ndef_message = models.TextField(blank=True)
    memdump = models.TextField(blank=True)
    timestamp = models.DateTimeField('time scanned')

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
