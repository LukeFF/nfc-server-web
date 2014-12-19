from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from nfctags.models import NfcTag, TagType

# Create your views here.
def index(request):
    tag_list = NfcTag.objects.order_by('timestamp')[:100]
    tag_types = TagType.objects.order_by('id')

    context = {'tag_list': tag_list, 'tag_types': tag_types}
    return render(request, 'index.html', context)

def detail(request, tag_id):
    tag = get_object_or_404(NfcTag, pk=tag_id)
    return render(request, 'index.html', {'tag': tag})
