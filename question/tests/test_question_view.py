from django.urls import reverse
from rest_framework.test import APITestCase
from agent.models import Agent
from customauth.models import MyUser
from django.utils import timezone
from rest_framework.authtoken.models import Token
from question.models import Question, Option


class TestQuestionCreate(APITestCase):
    """ test for question create """
    agent = None
    valid_data = None

    def setUp(self) -> None:
        user = MyUser.objects.create_user(
            email="agent@gmail.com", role="AGENT",
            password="newpassword"
        )

        self.agent = Agent.objects.create(
            name="agent", user=user,
            phone_number="1234567890",
            address_state="kerala",
            address_city="thrissur",
            address_pin="680511",
        )
        self.valid_data = {
            "text": "first question",
            "answer": "option id",
            'options': [
                    {'text': "first option"},
                    {'text': "second option"}
            ]
        }
        admin = MyUser.objects.create_user(
            email="admin@gmail.com", role="ADMIN",
            password="newpassword"
        )

    def test_question_create_return_401(self):
        """ test user is authenticated """
        response = self.client.post(
            reverse('create_question'), data=self.valid_data, format="json")
        assert response.status_code == 401

    def test_question_create_return_403(self):
        """ return 403 if not admin """
        token = Token.objects.get(user__email="admin@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(
            reverse('create_question'), data=self.valid_data, format="json")
        assert response.status_code == 403

    def test_question_create_return_201(self):
        """test question created with options """
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(
            reverse('create_question'), data=self.valid_data, format="json")
        assert response.status_code == 201
        assert Question.objects.first().options.count() == 2

    def test_question_update_return_200(self):
        """test question updated with options """
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        q = Question.objects.create(text="first question ", created_by=self.agent,
                                    answer="answer"
                                    )
        a = Option.objects.create(text="first", question=q)
        b = Option.objects.create(text="second", question=q)

        update_data = {
            "text": "updated text", "answer": "updated answer",
            "options": [
                    {"text": a.text},
                    {"text": "another option"}
            ]

        }
        response = self.client.put(
            reverse('update_question', kwargs={'pk': 1}), data=update_data, format="json")
        assert response.status_code == 200
        assert Option.objects.get(text="another option") is not None
