from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer, MyUser
# Create your views here.


class GetUserDetails(APIView):
    """ get user details"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        """ get user details """
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)
