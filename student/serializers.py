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
        if value is not None and re.search("^(\d{1,3}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$", value):
            return value
        raise serializers.ValidationError("phone number should be 10 digits ")

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("name should be greater than 3")

        return value
