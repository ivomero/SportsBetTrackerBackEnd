from .models import Bets
from .serializers import BetsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class BetsList(APIView):

    def get(self, request):
        bets = Bets.objects.all()
        serializer = Bets(bets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BetsDetail(APIView):

    def get_object(self, pk):
        try:
            return Bets.objects.get(pk=pk)
        except Bets.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        bets = self.get_object(pk)
        serializer = BetsSerializer(bets)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        bets = self.get_object(pk)
        serializer = BetsSerializer(bets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        bets = self.get_object(pk)
        bets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
