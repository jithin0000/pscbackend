from rest_framework import generics
from rest_framework import authentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
# Create your views here.
from fileupload.serializers import FileUploadSerializer
from customauth.permissions import AgentOnly


class FileUploadView(generics.CreateAPIView):
    """ create api view"""
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated,AgentOnly]
    authentication_classes =[TokenAuthentication]
    parser_classes = [MultiPartParser]


