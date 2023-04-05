from rest_framework import serializers
from .models import Album, Artist, Artistsong, Playlist, Playlistbyuser, Playlistbyusersong, Playlistsong, Playlistuser, Song, Topic, User, Usersongs

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'thumbnail_url', 'descripton', 'date_create', 'like']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'follow', 'thumbnail', 'alias']

class ArtistsongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistsong
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'title', 'thumbnail', 'topic', 'description']

class PlaylistbyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistbyuser
        fields = ['id', 'title', 'thumbnail', 'creator']

class PlaylistbyusersongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistbyusersong
        fields = '__all__'

class PlaylistsongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistsong
        fields = '__all__'

class PlaylistuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistuser
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ['id', 'title', 'audio', 'thumbnail', 'album', 'like']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'passwd', 'name', 'email', 'thumbnail']

class UsersongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersongs
        fields = '__all__'
