from customauth.models import MyUser
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from agent.models import Agent
from rest_framework.authtoken.models import Token


class TestAgentListView(APITestCase):
    normal_username = ""
    admin_username = ""

    def setUp(self) -> None:
        self.normal_username = "fake@gmail.com"
        MyUser.objects.create_user(
            email=self.normal_username,
            password="password"
        )
        self.admin_username = 'admin@gmail.com'
        MyUser.objects.create_superuser(
            email=self.admin_username,
            password="password"
        )

    def test_should_return_success_if_loggedin_as_admin(self):
        token = Token.objects.get(user__email=self.admin_username)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+token.key)
        response = self.client.get(reverse('agent'), format="json")
        assert response.status_code == 200

    def test_should_return_403_if_user_not_admin(self):
        token = Token.objects.get(user__email=self.normal_username)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+token.key)

        response = self.client.get(reverse('agent'), format="json")
        assert response.status_code == 403

    def test_should_return_401_if_no_user(self):
        response = self.client.get(reverse("agent"), format="json")
        assert response.status_code == 401
