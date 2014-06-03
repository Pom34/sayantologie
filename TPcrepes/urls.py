from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TPcrepes.views.home', name='home'),
    url(r'^miniurl/', include('miniurl.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
