from rest_framework.test import APITestCase
from accounts.models import User

class RegistrationTests(APITestCase):
    def test_registration(self):
        data ={
            "username": "Shiva",
            "email":"shiva@example.com",
            "password":"shiva123",
            "role":"Customer"
        }

        response = self.client.post("/api/auth/register/",data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username="Shiva").exists())

    def test_duplicate_username(self):
        data ={
            "username": "Shiva",
            "email":"vasi@example.com",
            "password":"vasi123",
            "role":"Customer"
        }
        User.objects.create_user(username="Shiva",email="shivaaa@example.com",password="123456",role="Customer")
       

        response = self.client.post("/api/auth/register/",data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.filter(username="Shiva").count(),1)

    def test_duplicate_email(self):
        data ={
            "username":"Shiva",
            "email":"Shiva@gmail.com",
            "password":"123456",
            "role":"Customer"
        }
        User.objects.create_user(username="vashi",email="Shiva@gmail.com",password="123456",role="Customer")

        response =self.client.post("/api/auth/register/",data)
        self.assertEqual(response.status_code,400)
        self.assertEqual(User.objects.filter(email="Shiva@gmail.com").count(),1)

    def test_missing_email(self):
        data ={
            "username":"Shiva",
            "password":"123456",
            "role":"Customer"

        }

        response = self.client.post("/api/auth/register/",data)

        self.assertEqual(response.status_code,400)
        self.assertFalse(User.objects.filter(username="Shiva").exists())

    def test_password_not_in_response(self):
        data ={
            "username":"Shiva",
            "email":"shiva@example.com",
            "password":"123456",
            "role":"Customer"
        }

        response = self.client.post("/api/auth/register/",data)

        self.assertEqual(response.status_code,201)
        self.assertNotIn("password",response.data)