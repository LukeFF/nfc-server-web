from django.conf.urls import patterns, url

from nfctags import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tag_uid>\w+)/$', views.history, name='history'),
    #url(r'^detail/(?P<tag_id>\d+)/$', views.detail, name='detail'),
    url(r'^add', views.add, name='add')
)
