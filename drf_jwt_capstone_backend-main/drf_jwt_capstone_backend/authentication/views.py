from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class ProfileList(APIView):

    def get(self, request):
        profiles = User.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
