from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404

# Create your views here.


class GameList(APIView):

    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetail(APIView):

    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        games = self.get_object(pk)
        serializer = GameSerializer(games)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        games = self.get_object(pk)
        serializer = GameSerializer(games, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        games = self.get_object(pk)
        games.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
