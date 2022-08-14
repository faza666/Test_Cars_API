from .test_set_up import TestSetUp
from django.urls import reverse
from rest_framework import status


class TestAPIViews(TestSetUp):
    def test_get_cars_view(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['access']}"
        )
        get_response = self.client.get(reverse("cars"))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(get_response.data, list)

    def test_cannot_get_cars_with_no_jwt_token_provided(self):
        get_response = self.client.get(reverse("cars"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_get_cars_with_wrong_jwt_token_provided(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['refresh']}"
        )
        get_response = self.client.get(reverse("cars"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_cars_view(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['access']}"
        )
        get_response = self.client.get(reverse("cars_all"))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(get_response.data, list)

    def test_cannot_get_all_cars_with_no_jwt_token_provided(self):
        get_response = self.client.get(reverse("cars_all"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_get_all_cars_with_wrong_jwt_token_provided(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['refresh']}"
        )
        get_response = self.client.get(reverse("cars_all"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_models_view(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['access']}"
        )
        get_response = self.client.get(reverse("models"))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(get_response.data, list)

    def test_cannot_get_models_with_no_jwt_token_provided(self):
        get_response = self.client.get(reverse("models"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_get_all_models_with_wrong_jwt_token_provided(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['refresh']}"
        )
        get_response = self.client.get(reverse("models"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_brands_view(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['access']}"
        )
        get_response = self.client.get(reverse("brands"))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(get_response.data, list)

    def test_cannot_get_brands_with_no_jwt_token_provided(self):
        get_response = self.client.get(reverse("brands"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_get_brands_with_wrong_jwt_token_provided(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.login_response.data['refresh']}"
        )
        get_response = self.client.get(reverse("brands"))
        self.assertEqual(get_response.status_code, status.HTTP_401_UNAUTHORIZED)
