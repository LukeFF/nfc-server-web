from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nfcserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('nfctags.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
