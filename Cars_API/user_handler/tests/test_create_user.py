from rest_framework.test import APITestCase
from django.urls import reverse


class TestCreateUserAPI(APITestCase):

    def setUp(self) -> None:
        self.username = 'test_user'
        self.email = 'test_user@gmail.com'
        self.password = 'Pa$$word!@'
        self.confirm_password = 'Pa$$word!@'

    def test_create_user(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], user_data.get("username"))
        self.assertEqual(response.data['email'], user_data.get("email"))

    def test_cannot_create_user_without_username(self):
        user_data = {
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"], ["This field is required."])

    def test_cannot_create_user_without_email(self):
        user_data = {
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["email"], ["This field is required."])

    def test_cannot_create_user_without_password_provided(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["password"], ["This field is required."])

    def test_cannot_create_user_without_password_confirmation_provided(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["confirm_password"], ["This field is required."])

    def test_cannot_create_user_with_password_confirmation_failed(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": "enother_pa$$word!@"
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["password"], ["Password fields didn't match."])

    def test_cannot_create_user_with_username_already_existing_in_database(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], user_data.get("username"))
        self.assertEqual(response.data['email'], user_data.get("email"))

        user_data_to_test = {
            "username": self.username,
            "email": "some.enother@gmail.com",
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data_to_test, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"], ["This field must be unique."])

    def test_cannot_create_user_with_email_already_existing_in_database(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], user_data.get("username"))
        self.assertEqual(response.data['email'], user_data.get("email"))

        user_data_to_test = {
            "username": "some_enother_username",
            "email": self.email,
            "password": self.password,
            "confirm_password": self.confirm_password
        }
        response = self.client.post(reverse('create'), user_data_to_test, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["email"], ["This field must be unique."])


