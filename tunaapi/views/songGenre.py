"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import SongGenre


class SongGenreView(ViewSet):
    """Tuna Api Song Genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Song Genre

        Returns:
            Response -- JSON serialized Genre
        """
        try:
            songGenre = SongGenre.objects.get(pk=pk)
            serializer = SongGenreSerializer(songGenre)
            return Response(serializer.data)
        except SongGenre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all SongGenres

        Returns:
            Response -- JSON serialized list of Genres
        """
        songGenres = SongGenre.objects.all()
        serializer = SongGenreSerializer(songGenres, many=True)
        return Response(serializer.data)
    
    #def create(self, request):
        #"""Handle POST operations
      
        #Returns:
           # Response -- JSON serialized song instance
        #"""
        #artist_id = Artist.objects.get(pk=request.data["artist_id"])

        #song = Song.objects.create(
        #title=request.data["title"],
        #artist_id=artist_id,
        #album=request.data["album"],
        #length=request.data["length"],
        #)
  
        #serializer = SongSerializer(song)
        #return Response(serializer.data)
    
    #def update(self, request, pk):
       # """Handle PUT requests for an song genre

       # Returns:
        #Response -- Empty body with 204 status code
       # """

        #song_genre = SongGenre.objects.get(pk=pk)
        #song_id = SongGenre.objects.get(pk=request.data["song_id"])
        #song_genre._song_id = song_id
        #genre_id = SongGenre.objects.get(pk=request.data["genre_id"])
        #song_genre._genre_id = genre_id
        #song_genre.save()

        #return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class SongGenreSerializer(serializers.ModelSerializer):
      """JSON serializer for song genres
      """
      class Meta:
        model = SongGenre
        fields = ('id', 'song_id', 'genre_id')
        depth = 1
