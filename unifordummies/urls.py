from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from default.views import ProgrammeListView


urlpatterns = patterns('',  # nopep8
    url(r'^$', 'default.views.index_page_view'),
    url(r'^search/$', 'default.views.search_page_view'),
    url(r'^search/(?P<id>\d+)$', 'default.views.search_cat_view'),
    url(r'^programme/(?P<prid>\d+)$', 'default.views.programme_view'),
    url(r'^programme/(?P<prid>\d+)/(?P<pid>\d+)$', 'default.views.posts_view'),
    url(r'^programme/(?P<prid>\d+)/post(?P<postid>\d+)$', 'default.views.post_view'),
    url(r'^programmes/', ProgrammeListView.as_view(), name='programmes'),

    url(r'^home/$', 'unifordummies.views.index_view', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
