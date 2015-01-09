from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from xml.dom.minidom import parseString
from django.utils.html import escape

from nfctags.models import NfcTag, TagType

# Create your views here.
def index(request):
    return redirect('tags/')
