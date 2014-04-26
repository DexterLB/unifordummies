from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from default.views import ProgrammeListView


urlpatterns = patterns('',  # nopep8
    # Examples:
    url(r'^home/$', 'unifordummies.views.index', name='index'),
    url(r'^test/$', 'unifordummies.views.test', name='test'),
    url(r'^post/$', 'unifordummies.views.post', name='post'),
    url(r'^posts/$', 'unifordummies.views.posts', name='posts'),
    url(r'^programmes/', ProgrammeListView.as_view(), name='programmes'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
