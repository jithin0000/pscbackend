from rest_framework import serializers
from rest_framework.test import APITestCase
from agent.models import Agent
from customauth.models import MyUser
from datetime import datetime,timedelta

from course.serializers import CourseSerializer

class TestCourseSerializer(APITestCase):
    """ test for course serializer """
    def test_course_serializer_is_valid_no_student_given(self):
        pass
    def test_course_serializer_status_is_created_if_date_not_reached(self):
        pass
    def test_show_error_course_serializer_start_date_is_less_than_today(self):
        agent = Agent.objects.create(
            user = MyUser.objects.create_user(email="test@gmail.com", password="password", role="AGENT"),
            name = "name",phone_number ="123456789",
            address_state ="kearala",
            address_city ="thrissur",
            address_pin ="6850123",
        )
        data = {
            "title":"first course",
            "description":"invalid description",
            "created_by": 1,
            "start_time": datetime.today()+ timedelta(-12),
            "end_time": datetime.today() + timedelta(24),
            "status": "CREATED"
        }
        serializer = CourseSerializer(data=data)
        assert serializer.is_valid() ==False

    def test_course_serializer_end_date_is_less_than_start_date(self):
        agent = Agent.objects.create(
            user = MyUser.objects.create_user(email="test@gmail.com", password="password", role="AGENT"),
            name = "name",phone_number ="123456789",
            address_state ="kearala",
            address_city ="thrissur",
            address_pin ="6850123",
        )
        data = {
            "title":"first course",
            "description":"invalid description",
            "created_by": 1,
            "start_time": datetime.today()+ timedelta(25),
            "end_time": datetime.today() + timedelta(24),
            "status": "CREATED"
        }
        serializer = CourseSerializer(data=data)
        assert serializer.is_valid() ==False
