from django.urls import reverse
from rest_framework.test import APITestCase
from course.models import Course
from customauth.models import MyUser
from rest_framework.authtoken.models import Token
from agent.models import Agent

from django.utils import timezone
from django.utils.timezone import timedelta

class TestCourseView(APITestCase):
    """ test for course view """
    admin =None
    agent = None
    def setUp(self) -> None:
        self.admin = MyUser.objects.create_user(
            email="admin@gmail.com", role="ADMIN",
            password="newpassword"
        )
        self.agent = Agent.objects.create(
            user = MyUser.objects.create_user(email="test@gmail.com", password="password", role="AGENT"),
            name = "name",phone_number ="123456789",
            address_state ="kearala",
            address_city ="thrissur",
            address_pin ="6850123",
        )      
    # // create course 
    def test_course_create_should_return_401(self):
        response = self.client.post(reverse('create_course'),format='json')
        assert response.status_code == 401

    def test_course_create_should_return_403(self):
        token = Token.objects.get(user__email="admin@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('create_course'),format='json')
        assert response.status_code == 403

    def test_course_create_should_return_201(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('create_course'),
        data = {
            "title":"first course",
            "description":"invalid description",
            "start_time": timezone.now()+ timedelta(21),
            "end_time": timezone.now() + timedelta(24),
        },format='json')
        course = Course.objects.get(title = 'first course')
        assert response.status_code == 201
        assert course.status == "CREATED"

     # get list of courses
    def test_course_list_should_return(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        Course.objects.create(
            title="course",description="this is description", start_time=timezone.now() +timedelta(2),
            end_time =timezone.now()+timedelta(4),
            created_by = self.agent
        )
        response = self.client.get(reverse('get_courses'),format="json")
        assert response.status_code == 200
     
    # course detail view  
    def test_course_detail_view_404(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('course_detail',kwargs={'pk': 1}),format="json")
        assert response.status_code == 404

    def test_course_detail_view_200(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        Course.objects.create(
            title="course",description="this is description", start_time=timezone.now() +timedelta(2),
            end_time =timezone.now()+timedelta(4),
            created_by = self.agent
        )
        response = self.client.get(reverse('course_detail',kwargs={'pk': 1}),format="json")
        assert response.status_code == 200
        assert response.data['id'] == 1
     

    # ====================== Course update view ========================================= #

    def test_course_udpate_view_200(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        course = Course.objects.create(
            title="course",description="this is description", start_time=timezone.now() +timedelta(2),
            end_time =timezone.now()+timedelta(4),
            created_by = self.agent
        )
        response = self.client.put(reverse('course_update',kwargs={'pk': 1}),
        data = {
            "title":"second course",
            "description":"invalid description",
            "start_time": course.start_time, 
            "end_time": course.end_time, 
        },format="json")
        assert response.status_code == 200
        assert response.data['title'] == 'second course'
 

    # ====================== Course delete view ========================================= #

    def test_course_udpate_view_204(self):
        token = Token.objects.get(user__email="test@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        Course.objects.create(
            title="course",description="this is description", start_time=timezone.now() +timedelta(2),
            end_time =timezone.now()+timedelta(4),
            created_by = self.agent
        )
        response = self.client.delete(reverse('course_delete',kwargs={'pk': 1}),format="json")
        assert response.status_code == 204
        assert Course.objects.count() ==0
 