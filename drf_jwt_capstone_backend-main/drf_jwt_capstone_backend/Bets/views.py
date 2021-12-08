from .models import Bet
from .serializers import BetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.


class BetList(APIView):

    def get(self, request):
        bets = Bet.objects.all()
        serializer = BetSerializer(bets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BetsDetail(APIView):

    def get_object(self, pk):
        try:
            return Bet.objects.get(pk=pk)
        except Bet.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        bets = self.get_object(pk)
        serializer = BetSerializer(bets)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        bets = self.get_object(pk)
        serializer = BetSerializer(bets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        bets = self.get_object(pk)
        bets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
