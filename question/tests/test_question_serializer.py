from customauth.models import MyUser
from rest_framework.test import APITestCase
from question.serializers import QuestionSerializer, OptionSerializer
from django.utils import timezone
from agent.models import Agent


class TestQuestionSerializer(APITestCase):
    """ Question serialiizer test"""

    def setUp(self) -> None:
        agent = MyUser.objects.create_user(
            email="agent@gmail.com", role="AGENT",
            password="newpassword"
        )

        Agent.objects.create(
            name="agent", user=agent,
            phone_number="1234567890",
            address_state="kerala",
            address_city="thrissur",
            address_pin="680511",
        )

    def test_question_serializer_is_valid(self):
        data = {
            "text": "first question",
            "created_by": 1,
            "answer": "option id",
            "created": timezone.now(),
            'options': [{
                'text': "first option",
            }]
        }
        serializer = QuestionSerializer(data=data)
        assert serializer.is_valid() == True
