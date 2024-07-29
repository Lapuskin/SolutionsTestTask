from django.contrib.auth.views import LoginView
from django.urls import path

from auth_module.views import SignUpView

urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]