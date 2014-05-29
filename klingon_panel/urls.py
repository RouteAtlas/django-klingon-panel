from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from klingon_panel.views import HomePageView, IndexPageView, ListPageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_klingon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^(?P<lang>[a-zA-Z_-]+)$', IndexPageView.as_view(), name='index'),
    
    url(r'^(?P<lang>[a-zA-Z_-]+)/(?P<section>[a-zA-Z_-]+)$', ListPageView.as_view(), name='list'),

    url(r'^admin/', include(admin.site.urls)),
)
