from django.urls.base import resolve
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils import timezone

from customauth.models import MyUser
from student.models import Student


class TestStudentView(APITestCase):
    """ test student veiw """

    def test_should_return_401(self):
        response = self.client.post(reverse('register_student'), data={
            "name": "first name"
        }, format="json")

        assert response.status_code == 401

    def test_should_return_403_if_not_Agent(self):
        admin = MyUser.objects.create_user(
            email="admin@gmail.com", role="ADMIN",
            password="newpassword"
        )
        token = Token.objects.get(user__email="admin@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('register_student'), data={
            "name": "first name"
        }, format="json")

        assert response.status_code == 403

    def test_should_return_201(self):
        agent = MyUser.objects.create_user(
            email="agent@gmail.com", role="AGENT",
            password="newpassword"
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('register_student'), data={
            "name": "first name",
            "phone_number": "1234567890",
            "email": "valid@gmail.com",
            "password": "newpassword"
        }, format="json")

        student = Student.objects.all().first()
        assert student.owner.email == "valid@gmail.com"
        assert student.added_by.email == "agent@gmail.com"
        assert response.status_code == 201

    def test_should_return_400_if_not_email_or_password(self):
        agent = MyUser.objects.create_user(
            email="agent@gmail.com", role="AGENT",
            password="newpassword"
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(reverse('register_student'), data={
            "name": "first name",
            "phone_number": "1234567890",
            "email": "valid@gmai",
            "password": ""
        }, format="json")

        assert response.status_code == 400


class TestStudentGetStudents(APITestCase):
    """ test case for get students """

    def test_should_return_401_get_student(self):
        response = self.client.get(reverse('get_students'), format="json")
        assert response.status_code == 401

    def test_should_return_403_get_student_if_not_agent(self):
        admin = MyUser.objects.create_user(
            email="admin@gmail.com", role="ADMIN",
            password="newpassword"
        )

        token = Token.objects.get(user__email="admin@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get_students'), format="json")
        assert response.status_code == 403

    def test_get_studens_return_200(self):
        agent = MyUser.objects.create_user(
            email="agent@gmail.com", role="AGENT",
            password="newpassword"
        )
        Student.objects.create(
            name="first name",
            owner=MyUser.objects.create_user(
                email="first@mgail.com", password="passwrdasdjlf",
                role="STUDENT"
            ),
            phone_number="1234567890",
            added_by=agent, created=timezone.now()
        )
        token = Token.objects.get(user__email="agent@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('get_students'), format="json")

        assert response.status_code == 200


class TestStudentDeleteView(APITestCase):
    """ test delete student by agent """

    admin = None
    agent = None
    student = None
    admin_token = None
    agent_token = None

    def setUp(self) -> None:
        self.admin = MyUser.objects.create(
            email="admin@gmail.com",
            password="password@",
            role="ADMIN"
        )
        self.agent = MyUser.objects.create(
            email="agent@gmail.com",
            password="password@",
            role="AGENT"
        )
        self.student = MyUser.objects.create(
            email="student@gmail.com",
            password="password@",
            role="STUDENT"
        )

        Student.objects.create(
            owner=self.student, name="student",
            phone_number="1234567890",
            added_by=self.agent,
            created=timezone.now()
        )
        self.admin_token = Token.objects.get(user__email=self.admin.email)
        self.agent_token = Token.objects.get(user__email=self.agent.email)

# ***************** Update *************************
    def test_update_student_return_401(self):
        response = self.client.put(
            reverse('update_student', kwargs={'pk': 1}), format="json")
        assert response.status_code == 401

    def test_update_student_return_403(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token "+self.admin_token.key)
        response = self.client.put(
            reverse("update_student", kwargs={"pk": 1}), format="json")
        assert response.status_code == 403

    def test_update_student_return_200(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token "+self.agent_token.key)
        stu = Student.objects.get(id=1)
        response = self.client.put(
            reverse("update_student", kwargs={"pk": 1}), data={
                "name": "updated name",
                "phone_number": stu.phone_number,
                "created": stu.created
            }, format="json")

        print(Student.objects.get(id=1).created)
        print(Student.objects.get(id=1).updated)
        assert response.status_code == 200
        assert Student.objects.get(id=1).name == "updated name"

 # ***************** Delete *************************

    def test_delete_student_return_401(self):
        response = self.client.delete(
            reverse('delete_student', kwargs={'pk': 1}), format="json")
        assert response.status_code == 401

    def test_delete_student_return_403(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token "+self.admin_token.key)
        response = self.client.delete(
            reverse("delete_student", kwargs={"pk": 1}), format="json")
        assert response.status_code == 403

    def test_delete_student_return_204(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="Token "+self.agent_token.key)
        response = self.client.delete(
            reverse("delete_student", kwargs={"pk": 1}), format="json")
        assert response.status_code == 204
        assert Student.objects.count() == 0
        assert MyUser.objects.get(email="agent@gmail.com") != None
