from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^analysis/', include('analysis.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
