from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateView.as_view(), name = 'register'),
    path("login/", LoginView.as_view(template_name = "login.html"), name = 'login'),
    path("logout/", LogoutView.as_view(next_page = "catalog:product_list"), name = 'logout'),
    path("email_confirm/<str:token>/", email_verification, name='email-confirm'),


]
