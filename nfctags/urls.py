from django.conf.urls import patterns, url

from nfctags import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tag_uid>\d+)/$', views.detail, name='detail'),
)
