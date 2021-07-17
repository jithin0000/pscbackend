from course.models import Course
from rest_framework import serializers

from django.utils import timezone

class CourseSerializer(serializers.ModelSerializer):
    """ serializer for course """
    class Meta:
        model = Course
        fields = ['id','title','description','start_time', 'end_time','students']

    def validate(self, data):
        if(data['end_time'] < data['start_time']):
            raise serializers.ValidationError("end time should be greater than start time ")
        return data

    def validate_start_time(self, value):
        if value is not None and value > timezone.now():
            return value
        raise serializers.ValidationError("start time should be greather than today")

