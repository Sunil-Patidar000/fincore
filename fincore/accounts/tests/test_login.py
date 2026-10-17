from django.template import response
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


class TokenRefreshTestCase(APITestCase):
        
        def test_refresh_token_success(self):
            User.objects.create_user(username="Shiva",email="shiva@example.com",password="123456",role="Customer")
            login_response =(self.client.post("/api/auth/login/",{"username": "Shiva", "password": "123456"}))
            token = login_response.data["refresh"]

            response = self.client.post("/api/auth/token/refresh/",{"refresh": token})
            

            self.assertEqual(response.status_code, 200)
            self.assertIn("access",response.data)

        def test_refresh_with_invalid_token(self):
            response = self.client.post("/api/auth/token/refresh/",{"refresh": "invalid_token"})
            self.assertEqual(response.status_code, 401)
            