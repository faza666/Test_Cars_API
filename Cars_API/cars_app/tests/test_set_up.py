from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self) -> None:

        self.user_data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "Pa$$word!@",
            "confirm_password": "Pa$$word!@",
        }
        self.client.post(reverse("create"), self.user_data, format="json")

        login_data = {
            "username": self.user_data.get("username"),
            "password": self.user_data.get("password"),
        }
        self.login_response = self.client.post(
            reverse("login"), login_data, format="json"
        )
