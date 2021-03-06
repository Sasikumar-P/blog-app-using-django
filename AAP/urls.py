from django.conf.urls import patterns, url

from AAP import views

urlpatterns = patterns('',
  url(r'^$', views.post_list, name='post_list'),
  url(r'^new$', views.post_create, name='post_new'),
  url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
)
