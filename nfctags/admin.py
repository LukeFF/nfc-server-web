from django.contrib import admin
from nfctags.models import NfcTag, TagType

# Register your models here.
class NfcTagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['uid', 'tagtype', 'memdump', 'reader', 'timestamp']}),
        ('NDEF', {'fields': ['ndef_version', 'ndef_readable', 'ndef_writeable', 'ndef_capacity', 'ndef_length', 'ndef_message']})
    ]
    list_display = ('uid', 'tagtype', 'reader', 'timestamp')
    search_fields = ['uid', 'memdump', 'reader']
class TagTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'speed')
admin.site.register(NfcTag, NfcTagAdmin)
admin.site.register(TagType, TagTypeAdmin)
