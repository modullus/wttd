# coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventex.core.views.homepage', name='homepage'),
    url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe'),
    url(r'^inscricao/(\d+)/$', 'eventex.subscriptions.views.detail', name='detail'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static',
    url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
)