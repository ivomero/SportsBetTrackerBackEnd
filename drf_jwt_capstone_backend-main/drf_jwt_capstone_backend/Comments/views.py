from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.


class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comments)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        comments = self.get_object(pk)
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
