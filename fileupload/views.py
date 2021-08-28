from rest_framework import generics
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
from fileupload.serializers import FileUploadSerializer
from customauth.permissions import AgentOnly


class FileUploadView(generics.CreateAPIView):
    """ create api view"""
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated,AgentOnly]
    authentication_classes =[JWTAuthentication]
    parser_classes = [MultiPartParser]



from rest_framework import status
import pytesseract
from PIL import Image
class ExtractTextFromImageView(APIView):
    """ extract questions from image"""
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated,AgentOnly]
    authentication_classes =[JWTAuthentication]
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            image = instance.image_url
            img = Image.open(image)
            text = pytesseract.image_to_string(img)
            return Response({"message": text},
            status = status.HTTP_200_OK )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
