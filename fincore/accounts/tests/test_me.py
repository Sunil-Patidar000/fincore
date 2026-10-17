from rest_framework.test import APITestCase
from accounts.models import User

class MeEndpointTestCase(APITestCase):
    def test_me_without_token(self):
        response=self.client.get("/api/auth/me/")
        self.assertEqual(response.status_code,401)


    def test_me_with_token(self):
        User.objects.create_user(username="Shiva",email="shiva@example.com",password="123456")

        login_response=self.client.post("/api/auth/login/",{"username":"Shiva","password":"123456"})
        access_token=login_response.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        response = self.client.get("/api/auth/me/")

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["username"],"Shiva")