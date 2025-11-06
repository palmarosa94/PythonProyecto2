from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *

urlpatterns = [
    path("login/", LoginView.as_view(template_name='accounts/login.htlm'), name='login'),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.htlm'), name='logout'),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_edit, name="profile_edit"),
]