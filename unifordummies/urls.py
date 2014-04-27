from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',  # nopep8
    url(r'^$', 'default.views.index_page_view'),
    url(r'^search/$', 'default.views.search_page_view'),
    url(r'^search/(?P<id>\d+)$', 'default.views.search_cat_view'),
    url(r'^programme/(?P<programme_id>\d+)$', 'default.views.programme_view',
        name="programme"),
    url(r'^programme/(?P<programme_id>\d+)/(?P<cat_id>\d+)$',
        'default.views.posts_view', name="post_category"),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('default.ajax',  # nopep8
    url(r'^post/(?P<post_id>\d+)/vote/(?P<direction>\w+)$', 'vote',
        name='post_vote'),
)
