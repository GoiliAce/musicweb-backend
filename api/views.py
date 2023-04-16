from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .zingapi import ZingMp3Async
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *
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

class PlaylistWithSongsDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistWithSongsSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        playlist = self.get_object(id)
        serializer = PlaylistWithSongsSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




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
    def get_object(self, alias):
        try:
            return Artist.objects.get(alias=alias)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, alias):
        artist = self.get_object(alias)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistWithSongsApiView(APIView):
    def get_object(self, alias):
        try:
            return Artist.objects.get(alias=alias)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        artist = self.get_object(alias)
        songs = Song.objects.filter(artists=artist).order_by('-listen')[:10] # Lấy 10 bài hát có lượt nghe cao nhất của nghệ sĩ này
        serializer = ArtistWithSongsSerializer(artist)
        artist_data = serializer.data
        artist_data['songs'] = SongForArtistSerializer(songs, many=True).data # Chuyển đổi các bài hát thành dữ liệu được serialize
        return Response(artist_data, status=status.HTTP_200_OK)
    
    def put(self, request, alias):
        artist = self.get_object(alias)
        serializer = ArtistWithSongsSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        serializer = SongForPlaylistSerializer(song)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    def put(self, request, id):
        song = self.get_object(id)        
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.get_object(id)
        song.delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

    
class CategoryListApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CategoryListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailApiView(APIView):
    def get_object(self, alias):
        try:
            return Category.objects.get(alias=alias)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, alias):
        category = self.get_object(alias)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, alias):
        category = self.get_object(alias)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, alias):
        category = self.get_object(alias)
        category.delete()
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

# user 
# import make_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
class UserRegisterApiView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)

from rest_framework_simplejwt.authentication import JWTAuthentication

class CurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
