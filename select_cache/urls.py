
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^album/(?P<album_id>[0-9]+)/$', views.album, name='album'),
	url(r'^genre/(?P<genre_id>[0-9]+)/$', views.genre, name='genre')
]

