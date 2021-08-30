from customauth.models import MyUser
from rest_framework import serializers
from .models import Student
import re


class StudentSerializer(serializers.ModelSerializer):
    """ serializer for model student """
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    added_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"

    def validate_phone_number(self, value):
        if value is not None and re.search("^(\d{1,3}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{3}$", value):
            return value
        raise serializers.ValidationError("phone number should be 10 or 12 digits ")

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("name should be greater than 3")

        return value


class UserSerializerForStudent(serializers.ModelSerializer):
    """ serializer of user, name,email, last login time """
    class Meta:
        model = MyUser
        fields =['email']

class StudentListResponseSerializer(serializers.ModelSerializer):
    """ serializer for showing student list"""
    owner = UserSerializerForStudent(read_only=True)
    added_by = UserSerializerForStudent(read_only=True)
    courses_count = serializers.SerializerMethodField()
    class Meta:
        model=Student
        fields ="__all__"

    def get_courses_count(self,obj):
        return obj.course_set.count()