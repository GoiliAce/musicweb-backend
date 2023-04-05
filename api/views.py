from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .zingapi import ZingMp3Async
from .models import Album, Artist, Artistsong, Playlist, Playlistbyuser, Playlistbyusersong, Playlistsong, Playlistuser, Song, Topic, User, Usersongs
from .serializers import AlbumSerializer, ArtistSerializer, ArtistsongSerializer, PlaylistSerializer, PlaylistbyuserSerializer, PlaylistbyusersongSerializer, PlaylistsongSerializer, PlaylistuserSerializer, SongSerializer, TopicSerializer, UserSerializer, UsersongsSerializer

class TopicListApiView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data, )
    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TopicDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Topic.objects.get(id=id)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        topic = self.get_object(id)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        topic = self.get_object(id)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistListApiView(APIView):
    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TopicPlaylistListApiView(APIView):
    def get(self, request, id):
        playlists = Playlist.objects.filter(topic=id)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlaylistDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        playlist = self.get_object(id)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PlaylistSongsListApiView(APIView):
    def get(self, request, id):
        try:
            playlist = Playlist.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        songs = playlist.songs.all()  # get all artists associated with the song
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class AlbumListApiView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AlbumDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        album = self.get_object(id)
        serializer = AlbumSerializer(album)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        album = self.get_object(id)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        album = self.get_object(id)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ArtistListApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ArtistDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Artist.objects.get(id=id)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        artist = self.get_object(id)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        artist = self.get_object(id)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        artist = self.get_object(id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SongListApiView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SongDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        song = self.get_object(id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SongArtistsApiView(APIView):
    def get(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        artists = song.artists.all()  # get all artists associated with the song
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            song.artists.add(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        try:
            song = Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        song.artists.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistSongsApiView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        songs = artist.songs.all()  # get all songs associated with the artist
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            artist.songs.add(serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        artist.songs.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.http import JsonResponse
from asgiref.sync import async_to_sync
async def getAudio(request, id):
    zi = ZingMp3Async()
    url = await zi.getAudio(id)
    data = {
        'url': url
    }
    return JsonResponse(data)

def AudioApiView(request, id):
    data = async_to_sync(getAudio)(request, id)
    return data






