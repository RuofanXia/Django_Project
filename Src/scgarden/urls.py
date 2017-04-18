from django.conf.urls import patterns, include, url

from scgarden import views

urlpatterns = patterns('',
	url(r'^$', views.scgarden),
)