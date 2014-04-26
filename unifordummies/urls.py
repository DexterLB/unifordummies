from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',  # nopep8
    # Examples:
    url(r'^$', 'unifordummies.views.index', name='index'),
    url(r'^test$', 'unifordummies.views.test', name='test'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
