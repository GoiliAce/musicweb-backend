from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/topic/playlists',views.TopicListApiView.as_view()),
    path('api/albums',views.AlbumListApiView.as_view()),
    path('api/albums/<str:id>',views.AlbumDetailApiView.as_view()),
    path('api/artists',views.ArtistListApiView.as_view()),
    path('api/playlists',views.PlaylistListApiView.as_view()),
    path('api/playlists/<str:id>',views.PlaylistDetailApiView.as_view()),
    path("api/playlist/<str:id>", views.PlaylistWithSongsDetailApiView.as_view(), name=""),
    path('api/songs',views.SongListApiView.as_view()),
    path('api/song/<str:id>',views.SongDetailApiView.as_view()),
    path('api/artist/<str:alias>',views.ArtistWithSongsApiView.as_view()),
    path('api/categories', views.CategoryListApiView.as_view()),
    path('api/category/<str:alias>',views.CategoryDetailApiView.as_view()),
    path('api/audio/<str:id>',views.AudioApiView, name="audio"),
]
