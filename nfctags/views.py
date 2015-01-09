from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from xml.dom.minidom import parseString
from django.utils.html import escape

from nfctags.models import NfcTag, TagType

# Create your views here.
def index(request):
    if request.method == 'POST':
        xml = request.POST['xml']
        doc = parseString(xml)

        nfctags = doc.getElementsByTagName('nfctag')
        for tag in nfctags:
            tagtype = tag.getAttribute('type')
            if tagtype == 'Type2Tag':
                tagtype = 2
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
        tag.message = tag.ndef_message.decode('hex').decode('latin1')
    return render(request, 'history.html', {'tags': tags})

def add(request):
    return render(request, 'add.html')
