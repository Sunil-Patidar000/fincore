from rest_framework.test import APITestCase
from accounts.models import User


class LoginTestCase(APITestCase):
    def test_Login(self):
        data ={
            "username": "Shiva",
            "email":"shiva@example.com",
            "password":"123456",
            "role":"Customer"
        }

        User.objects.create_user(username="Shiva",email="shiva@example.com",password="123456",role="Customer")

        response = self.client.post("/api/auth/login/",data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_wrong_password(self):
        data ={
            "username": "Shiva",
            "email":"shiva@example.com",
            "password":"wrongpassword",
            "role":"Customer"
        }

        User.objects.create_user(username="Shiva",email="shiva@example.com",password="123456",role="Customer")

        response = self.client.post("/api/auth/login/",data)

        self.assertEqual(response.status_code, 401)