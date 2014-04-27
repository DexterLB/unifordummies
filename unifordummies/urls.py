from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from default.views import ProgrammeListView


urlpatterns = patterns('',  # nopep8
    url(r'^$', 'unifordummies.views.index_page_view'),
    url(r'^search/$', 'unifordummies.views.search_page_view'),
    url(r'^search/(?P<id>\d+)$', 'unifordummies.views.search_cat_view'),
    url(r'^programme/(?P<prid>\d+)$', 'unifordummies.views.programme_view'),
    url(r'^programme/(?P<prid>\d+)/(?P<pid>\d+)$', 'unifordummies.views.posts_view'),
    url(r'^programme/(?P<prid>\d+)/post(?P<postid>\d+)$', 'unifordummies.views.post_view'),
    url(r'^programmes/', ProgrammeListView.as_view(), name='programmes'),

    url(r'^admin/', include(admin.site.urls)),
)
