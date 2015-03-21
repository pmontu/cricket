from django.conf.urls import patterns, url

from analysis.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^team/post\.json$', team_post),
    url(r'^teams\.json$', teams),
    url(r'^team/delete\.json$', delete_team),

)
