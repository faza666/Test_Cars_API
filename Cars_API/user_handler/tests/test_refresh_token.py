from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestRefreshTokenAPI(APITestCase):
    def test_refresh_user_access_token(self):

        self.user_data = {
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "Pa$$word!@",
            "confirm_password": "Pa$$word!@",
        }
        create_response = self.client.post(
            reverse("create"), self.user_data, format="json"
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            create_response.data["username"], self.user_data.get("username")
        )
        self.assertEqual(create_response.data["email"], self.user_data.get("email"))

        login_data = {
            "username": self.user_data.get("username"),
            "password": self.user_data.get("password"),
        }
        login_response = self.client.post(reverse("login"), login_data, format="json")
        self.assertContains(login_response, "refresh", 1, status.HTTP_200_OK)
        self.assertContains(login_response, "access", 1, status.HTTP_200_OK)

        refresh_data = {
            "refresh": login_response.data["refresh"],
        }
        refresh_response = self.client.post(
            reverse("token_refresh"), refresh_data, format="json"
        )
        self.assertContains(refresh_response, "access", 1, status.HTTP_200_OK)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh_response.data['access']}"
        )
        get_response = self.client.get(reverse("cars"))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(get_response.data, list)
