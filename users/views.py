from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer