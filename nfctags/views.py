import sys
import os
import string

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from xml.dom.minidom import parseString
from django.utils.html import escape

from nfctags.models import NfcTag, TagType

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../nfcpy')
import nfc

def format_hex(data, w=16):
    printable = string.digits + string.letters + string.punctuation + ' '
    if type(data) is not type(str()):
        data = str(data)
    s = []
    for i in range(0, len(data), w):
        s.append("  {offset:04x}: ".format(offset=i))
        s[-1] += ' '.join(["%02x" % ord(c) for c in data[i:i+w]]) + ' '
        s[-1] += (8 + w*3 - len(s[-1])) * ' '
        s[-1] += ''.join([c if c in printable else '.' for c in data[i:i+w]])
    return '\n'.join(s)


# Create your views here.
def index(request):
    if request.method == 'POST':
        xml = request.POST['xml']
        doc = parseString(xml)

        nfctags = doc.getElementsByTagName('nfctag')
        for tag in nfctags:
            tagtype = tag.getAttribute('type')
            if tagtype == 'Type1Tag':
                tagtype = 1
            elif tagtype == 'Type2Tag':
                tagtype = 2
            elif tagtype == 'Type3Tag':
                tagtype = 3
            elif tagtype == 'Type4Tag':
                tagtype = 4
            else:
                tagtype = 0

            uid = tag.getElementsByTagName('uid')[0].firstChild.data
            timestamp = tag.getElementsByTagName('timestamp')[0].firstChild.data

            newTag = NfcTag.objects.create(uid=uid, tagtype=TagType.objects.get(pk=tagtype), timestamp=timestamp)
            newTag.atq = tag.getElementsByTagName('atq')[0].firstChild.data
            newTag.sak = tag.getElementsByTagName('sak')[0].firstChild.data
            newTag.reader = tag.getElementsByTagName('reader')[0].firstChild.data

            newTag.ndef_version = tag.getElementsByTagName('version')[0].firstChild.data
            newTag.ndef_readable = tag.getElementsByTagName('readable')[0].firstChild.data
            newTag.ndef_writeable = tag.getElementsByTagName('writeable')[0].firstChild.data
            newTag.ndef_capacity = tag.getElementsByTagName('capacity')[0].firstChild.data
            newTag.ndef_length = tag.getElementsByTagName('length')[0].firstChild.data
            newTag.ndef_message = tag.getElementsByTagName('message')[0].firstChild.data

            newTag.save()
        return HttpResponse('Successfully saved data on server')

    else:
        tag_list = NfcTag.objects.order_by('-timestamp')
        tag_types = TagType.objects.order_by('id')

        context = {'tag_list': tag_list, 'tag_types': tag_types}
        return render(request, 'taglist.html', context)

def history(request, tag_uid):
    tags = NfcTag.objects.filter(uid=tag_uid)
    for tag in tags:
        tag.message = nfc.ndef.Message(tag.ndef_message.decode('hex'))
        tag.ndef_message = format_hex(tag.ndef_message.decode('hex'))
    return render(request, 'history.html', {'tags': tags})

def add(request):
    return render(request, 'add.html')
