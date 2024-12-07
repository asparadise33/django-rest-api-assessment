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
           # genres = Genre.objects.filter(songgenres__song_id=song)
           # print(genres)
           #dunderscores gives us the one step access to the song connects the join table
            
            serializer = SongSerializer(song)
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
        artist_id = Artist.objects.get(pk=request.data["artist_id"])

        song = Song.objects.create(
        title=request.data["title"],
        artist_id=artist_id,
        album=request.data["album"],
        length=request.data["length"],
        )
  
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a song

        Returns:
        Response -- Empty body with 204 status code
        """

        song = Song.objects.get(pk=pk)
        song.title=request.data["title"]
        artist_id = Artist.objects.get(pk=request.data["artist_id"])
        song._artist_id = artist_id
        song.album=request.data["album"]
        song.length=request.data["length"]
        song.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    
   
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for songs
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length', 'songgenres')
        depth = 2
