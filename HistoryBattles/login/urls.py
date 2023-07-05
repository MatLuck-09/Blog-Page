from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('', views.loginUsers, name="Login" ),

    path('register/', views.register, name="Register"),

    path('logout/', LogoutView.as_view(template_name = "login/login.html"), name="Logout"),
]