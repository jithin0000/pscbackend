from rest_framework.test import APITestCase
from student.serializers import StudentSerializer


class TestStudentSerializer(APITestCase):

    def test_serializer_is_valid(self):
        data = {
            "name": "first name",
            "phone_number": "1234567890"
        }
        serializer = StudentSerializer(data=data)
        assert serializer.is_valid() == True
