from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

 
        url(r'^$', views.frontend, name ='frontend'),
        #urls Género
        url(r'^discografica/genero/$', views.index_genero, name ='index_genero'),
        url(r'^discografica/genero/new/$', views.genero_new, name='genero_new'),
        url(r'^discografica/genero/(?P<pk>[0-9]+)/edit/$', views.genero_edit, name='genero_edit'),
        url(r'^discografica/genero/show/(?P<pk>[0-9]+)/$', views.genero_show, name='genero_show'),
        url(r'^discografica/genero/(?P<pk>\d+)/remove/$', views.genero_remove, name='genero_remove'),
        #urls para Artista
        url(r'^discografica/artista/$', views.artista_index, name ='artista_index'),
        url(r'^discografica/artista/new/$', views.artista_new, name='artista_new'),
        url(r'^discografica/artista/(?P<pk>[0-9]+)/edit/$', views.artista_edit, name='artista_edit'),
        url(r'^discografica/artista/show/(?P<pk>[0-9]+)/$', views.artista_show, name='artista_show'),
        url(r'^discografica/artista/(?P<pk>\d+)/remove/$', views.artista_remove, name='artista_remove'),
        #urls para Album
        url(r'^discografica/album/$', views.album_index, name ='album_index'),
        url(r'^discografica/album/new/$', views.album_new, name='album_new'),
        url(r'^discografica/album/(?P<pk>[0-9]+)/edit/$', views.album_edit, name='album_edit'),
        url(r'^discografica/album/show/(?P<pk>[0-9]+)/$', views.album_show, name='album_show'),
        url(r'^discografica/album/(?P<pk>\d+)/remove/$', views.album_remove, name='album_remove'),
        #urls para Cancion
        url(r'^discografica/cancion/$', views.cancion_index, name ='cancion_index'),
        url(r'^discografica/nueva/$', views.cancion_nueva, name='cancion_nueva'),
        url(r'^discografica/cancion/(?P<pk>[0-9]+)/edit/$', views.cancion_edit, name='cancion_edit'),
        url(r'^discografica/cancion/show/(?P<pk>[0-9]+)/$', views.cancion_show, name='cancion_show'),
        url(r'^discografica/cancion/(?P<pk>\d+)/remove/$', views.cancion_remove, name='cancion_remove'),
        #urls para vocalista
        url(r'^discografica/vocalista/$', views.vocalista_index, name ='vocalista_index'),
        url(r'^discografica/vocalista/new/$', views.vocalista_new, name='vocalista_new'),
        url(r'^discografica/vocalista/(?P<pk>[0-9]+)/edit/$', views.vocalista_edit, name='vocalista_edit'),
        url(r'^discografica/vocalista/show/(?P<pk>[0-9]+)/$', views.vocalista_show, name='vocalista_show'),
        url(r'^discografica/vocalista/(?P<pk>\d+)/remove/$', views.vocalista_remove, name='vocalista_remove'),
    ]
