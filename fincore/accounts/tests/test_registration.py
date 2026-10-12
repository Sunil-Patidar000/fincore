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