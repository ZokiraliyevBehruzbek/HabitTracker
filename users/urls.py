from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.views import RegisterView


urlpatterns = (
    [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ]
)
