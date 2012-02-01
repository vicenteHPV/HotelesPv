# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'HotelesPv.motor.views.home',{'saludo':'Y Sigo Aprendiendo Python y más haber', 'opcion':'Segunda Opcion'} ),
    # url(r'^HotelesPv/', include('HotelesPv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recursos/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT ,'show_indexes':True }),
)
