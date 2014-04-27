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

<<<<<<< HEAD
    url(r'^$', 'default.views.index_page_view'),
    url(r'^search/$', 'default.views.search_page_view'),
    url(r'^search/(?P<id>\d+)$', 'default.views.search_cat_view'),
    url(r'^programme/(?P<programme_id>\d+)$', 'default.views.programme_view'),
    url(r'^programme/(?P<programme_id>\d+)/(?P<cat_id>\d+)$',
        'default.views.posts_view'),

=======
>>>>>>> 4282a999a0f469fbea71e8fabf70f795bede2352
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('default.ajax',  # nopep8
    url(r'^post/(?P<post_id>\d+)/vote/(?P<direction>\w+)$', 'vote',
        name='post_vote'),
)
