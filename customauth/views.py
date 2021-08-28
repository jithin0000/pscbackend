from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Create your views here.
from .serializers import PscTokenSerializer, TokenObtainPairResponseSerializer, TokenRefreshResponseSerializer, TokenVerifyResponseSerializer, UserSerializer

class GetUserDetails(APIView):
    """ get user details"""
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        """ get user details """
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)

class PscJwtTokenPairView(TokenObtainPairView):
    """ view for jwt token """
    serializer_class = PscTokenSerializer


""" ========================== jwt views for swagger ======================"""
from drf_yasg.utils import swagger_auto_schema

class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)