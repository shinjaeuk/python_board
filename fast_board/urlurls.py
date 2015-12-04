from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.create_post, name='create'),
	url(r'^list/$', views.list_posts, name='list'),
	url(r'^view/(?P<pk>[0-9]+)/$', views.view_post, name='view'),
	url(r'^view/(?P<pk>[0-9]+)/edit/$', views.edit_post, name='edit'),
	url(r'^comment/(?P<pk>[0-9]+)/delete/$', views.delet_comment, name='comment_delete'),
	url(r'^comment/create/$', views.create_comment, name='comment_create'),
]