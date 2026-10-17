from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from accounts.serializers import RegisterSerializers,UserSerializer
from accounts.models import User

# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]


class MeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user