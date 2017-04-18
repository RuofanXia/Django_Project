from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Garden.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('mainpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('mainpage.urls')),
    url(r'^school_and_children_garden_link/', include('scgarden.urls')),
    url(r'^playful_plants/', include('playfulPlants.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
)
