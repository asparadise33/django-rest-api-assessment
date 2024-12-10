"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Genre, Artist

class SongView(ViewSet):
    """Tuna Api Songview"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Song

        Returns:
            Response -- JSON serialized Song
        """
        try:
            song = Song.objects.get(pk=pk)
            genres = Genre.objects.filter(songs__id=song.id)
            song.genres=genres
           
           
            serializer = SongDetailSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all Songs

        Returns:
            Response -- JSON serialized list of Songs
        """
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
      
        Returns:
            Response -- JSON serialized song instance
        """
        artist = Artist.objects.get(pk=request.data["artist_id"])

        song = Song.objects.create(
        title=request.data["title"],
        artist=artist,
        album=request.data["album"],
        length=request.data["length"],
        )
  
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a song

        Returns:
        Response -- Empty body with 204 status code
        """

        song = Song.objects.get(pk=pk)
        song.title=request.data["title"]
        artist = Artist.objects.get(pk=request.data["artist_id"])
        song.artist = artist
        song.album=request.data["album"]
        song.length=request.data["length"]
        song.save()
        serializer = SongSerializer(song)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
   
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        depth = 2
class ArtistSerialzer(serializers.ModelSerializer):
    """JSON serializer for artist details
    """
    class Meta:
        model = Artist
        fields = ('id','name', 'age', 'bio')

class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genre details
    """
    class Meta:
        model = Genre
        fields = ('id', 'description')


class SongDetailSerializer(serializers.ModelSerializer):
    """JSON serializer for song details
    """ 
    artist = ArtistSerialzer()
    genres = GenreSerializer(many=True)
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length', 'genres')
