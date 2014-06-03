from django.conf.urls import patterns, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('miniurl.views',
    #url(r'^$', 'TPcrepes.views.home', name='home'),
    url(r'^all/$', 'display_miniurls'),
    url(r'^new/$', 'shorten_url', name='create_new_url'),
    url(r'^(?P<code_in_url>\w{6})/$', 'redirect_from_code', name='url_redirection'),
    url(r'^','redirect_to_allurl_for_non_existent_url'),
    #url(r'^admin/', include(admin.site.urls)),
)