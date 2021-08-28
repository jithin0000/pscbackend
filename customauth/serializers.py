from rest_framework import serializers,status
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'role']
    

""" ==================  serizlier for custominzing token ======================= """
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PscTokenSerializer(TokenObtainPairSerializer):
    """ serializer for customizing token """

    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)

        # add user role
        token['role']=user.role
        return token


""" ==================  serializer for swagger view ======================= """

class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()

class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
