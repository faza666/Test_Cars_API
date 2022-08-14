from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestLoginUserAPI(APITestCase):
    def setUp(self) -> None:

        self.user_data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "Pa$$word!@",
            "confirm_password": "Pa$$word!@",
        }
        self.client.post(reverse("create"), self.user_data, format="json")

    def test_login_user_with_username(self):
        login_data = {
            "username": self.user_data.get("username"),
            "password": self.user_data.get("password"),
        }
        response = self.client.post(reverse("login"), login_data, format="json")
        self.assertContains(response, "refresh", 1, status.HTTP_200_OK)
        self.assertContains(response, "access", 1, status.HTTP_200_OK)

    def test_login_user_with_email(self):
        login_data = {
            "username": self.user_data.get("email"),
            "password": self.user_data.get("password"),
        }
        response = self.client.post(reverse("login"), login_data, format="json")
        self.assertContains(response, "refresh", 1, status.HTTP_200_OK)
        self.assertContains(response, "access", 1, status.HTTP_200_OK)

    def test_cannot_login_user_without_username_or_email_provided(self):
        login_data = {"password": self.user_data.get("password")}
        response = self.client.post(reverse("login"), login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["username"], ["This field is required."])

    def test_cannot_login_user_without_password_provided(self):
        login_data = {"username": self.user_data.get("email")}
        response = self.client.post(reverse("login"), login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"], ["This field is required."])

    def test_cannot_login_user_with_password_check_failed(self):
        login_data = {
            "username": self.user_data.get("email"),
            "password": "123 456 789",
        }
        response = self.client.post(reverse("login"), login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"],
            "No active account found with the given credentials",
        )
