from rest_framework import serializers
from .models import Agent
import re


class AgentSerializer(serializers.ModelSerializer):
    """ serializer for Agent Model"""
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Agent
        fields = ['name', 'phone_number', 'user',
                  'address_state', 'address_city', 'address_pin']

    def validate_phone_number(self, value):
        if value is not None and re.search("^(\d{1,3}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$", value):
            return value
        raise serializers.ValidationError("phone number should be 10 digits ")

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("name should be greater than 3")

        return value
