from rest_framework import serializers
from .models import *
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistsongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistsong
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistbyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlistbyuser
        fields = '__all__'

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
    class Meta:
        model = Song
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UsersongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersongs
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ArtistForSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name','alias']
class SongForPlaylistSerializer(serializers.ModelSerializer):
    artists = ArtistForSongSerializer(many=True)
    album = AlbumSerializer() # serialize album thông qua AlbumSerializer
    class Meta:
        model = Song
        fields = ['id', 'title', 'artists','thumbnail', 'album', 'audio','duration']
class PlaylistWithSongsSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistSerializer(many=True)
    class Meta:
        model = Playlist
        fields = '__all__'

class AlbumsWithSongsSerializer(serializers.ModelSerializer):
    songs = SongForPlaylistSerializer(many=True)
    class Meta:
        model = Album
        fields = '__all__'
class SongForArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', 'audio']

class ArtistWithSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','alias']