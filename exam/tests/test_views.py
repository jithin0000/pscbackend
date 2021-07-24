from django.urls.base import reverse
from rest_framework.test import APITestCase
from agent.models import Agent
from customauth.models import MyUser
from rest_framework.authtoken.models import Token
from exam.models import Exam

from django.utils import timezone, timesince



class TestExamView(APITestCase):
    """ test for exam"""
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
            "name": "first exam",
            "start_time": timezone.now()+timezone.timedelta(1),
            "end_time": timezone.now()+timezone.timedelta(2),
            "total_questions": 12,
            "mark_per_question": 1,
            "minus_mark_per_question": -2,

        }
        admin = MyUser.objects.create_user(
            email="admin@gmail.com", role="ADMIN",
            password="newpassword"
        )
    
    def testCreateExam_return_401(self):
        response = self.client.post(reverse('exam_create'),data=self.valid_data,format="json")
        assert response.status_code == 401

    def testCreateExam_return_403(self):
        token = Token.objects.get(user__email="admin@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('exam_create'),data=self.valid_data,format="json")
        assert response.status_code == 403

    def testCreateExam_return_201(self):
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('exam_create'),data=self.valid_data,format="json")
        assert response.status_code == 201
        assert Exam.objects.first().id ==1

    
    # ================= GET EXAM ===============
    def test_get_exam_should_return_200(self):
        Exam.objects.create(
            name="name",start_time=timezone.now()+timezone.timedelta(2),
            end_time=timezone.now()+timezone.timedelta(2),
            total_questions= 12,
            mark_per_question = 1,
            minus_mark_per_question =  -2,
            created_by = self.agent
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('exam_list'),format="json")
        assert response.status_code == 200

    # ================= Detail of EXAM ===============
    def test_get_detail_exam_should_return_404(self):
        Exam.objects.create(
            name="name",start_time=timezone.now()+timezone.timedelta(2),
            end_time=timezone.now()+timezone.timedelta(2),
            total_questions= 12,
            mark_per_question = 1,
            minus_mark_per_question =  -2,
            created_by = self.agent
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('exam_detail',kwargs={'pk':2}),format="json")
        assert response.status_code == 404

    def test_get_exam_detail_should_return_200(self):
        Exam.objects.create(
            name="name",start_time=timezone.now()+timezone.timedelta(2),
            end_time=timezone.now()+timezone.timedelta(2),
            total_questions= 12,
            mark_per_question = 1,
            minus_mark_per_question =  -2,
            created_by = self.agent
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('exam_detail',kwargs={'pk':1}),format="json")
        assert response.status_code == 200


    # ================= update  EXAM ===============
    def test_get_updatel_exam_should_return_200(self):
        Exam.objects.create(
            name="name",start_time=timezone.now()+timezone.timedelta(2),
            end_time=timezone.now()+timezone.timedelta(2),
            total_questions= 12,
            mark_per_question = 1,
            minus_mark_per_question =  -2,
            created_by = self.agent
        )

        updated_data = {
            "name": "updated exam",
            "start_time": timezone.now()+timezone.timedelta(1),
            "end_time": timezone.now()+timezone.timedelta(2),
            "total_questions": 12,
            "mark_per_question": 1,
            "minus_mark_per_question": -2,
        }
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.put(reverse('exam_update',kwargs={'pk':1}), data=updated_data,format="json")
        assert response.status_code == 200
        assert Exam.objects.first().name == "updated exam"

    # ================= delete EXAM ===============
    def test_get_delete_exam_should_return_200(self):
        Exam.objects.create(
            name="name",start_time=timezone.now()+timezone.timedelta(2),
            end_time=timezone.now()+timezone.timedelta(2),
            total_questions= 12,
            mark_per_question = 1,
            minus_mark_per_question =  -2,
            created_by = self.agent
        )

        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.delete(reverse('exam_delete',kwargs={'pk':1}),format="json")
        assert response.status_code == 204
        assert Exam.objects.count() == 0
