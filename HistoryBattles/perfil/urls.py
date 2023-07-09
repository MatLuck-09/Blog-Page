from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('', views.perfilview, name="Perfil" ),

    path('editar/', views.editarPerfil, name="Editar" ),

    path('changePassword/', views.changePassword, name="Cambiar Password" ),

    path('avatar/', views.editAvatar, name="Editar Avatar" ),

]
