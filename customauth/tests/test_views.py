from django.urls import reverse
from customauth.models import MyUser
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class TestAuthView(APITestCase):

    def test_should_return_401(self):
        response = self.client.get(reverse("user_detail"), format="json")
        assert response.status_code == 401

    def test_should_return_user(self):
        MyUser.objects.create_user(
            email="fake@gmail.com", password="newpassword")
        token = Token.objects.get(user__email="fake@gmail.com")
        self.client.credentials(HTTP_AUTHORIZATION="Token "+token.key)
        response = self.client.get(reverse('user_detail'), format="json")
        assert response.status_code == 200
        assert response.data['email'] == "fake@gmail.com"
