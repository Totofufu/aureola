from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Psychedelic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Psychedelic.views.loadIndex'),
    url(r'^supportee$', 'Psychedelic.views.profilePage'),
    url(r'^supporter$', 'Psychedelic.views.supporterPage'),
    url(r'^login$', 'Psychedelic.views.loginPage'),
    url(r'^1/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'Psychedelic.views.aboutPage'),
    url(r'^create_supportee/$', 'Psychedelic.views.createSupporteePage'),
    url(r'^create_supporter/$', 'Psychedelic.views.createSupporterPage'),
)
