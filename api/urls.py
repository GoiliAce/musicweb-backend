from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/topics',views.TopicListApiView.as_view()),
    path('api/topics/<str:id>',views.TopicDetailApiView.as_view()),
    path('api/topics/playlist/<str:id>',views.TopicPlaylistListApiView.as_view()),
    path('api/albums',views.AlbumListApiView.as_view()),
    path('api/albums/<str:id>',views.AlbumDetailApiView.as_view()),
    path('api/artists',views.ArtistListApiView.as_view()),
    path('api/artists/<str:id>',views.ArtistDetailApiView.as_view()),
    path('api/playlists',views.PlaylistListApiView.as_view()),
    path('api/playlists/<str:id>',views.PlaylistDetailApiView.as_view()),
    path("api/playlists/songs/<str:id>", views.PlaylistSongsListApiView.as_view(), name=""),
    path('api/songs',views.SongListApiView.as_view()),
    path('api/songs/<str:id>',views.SongDetailApiView.as_view()),
    path('api/songs/artist/<str:id>',views.SongArtistsApiView.as_view()),
    path('artist/song/api/<str:id>',views.ArtistSongsApiView.as_view()),
    path('api/songs/audio/<str:id>',views.AudioApiView, name="audio"),
]
