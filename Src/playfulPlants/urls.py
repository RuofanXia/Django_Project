from django.conf.urls import patterns, include, url

from playfulPlants import views

urlpatterns = patterns('',
	url(r'^$', views.playfulPlants),
)