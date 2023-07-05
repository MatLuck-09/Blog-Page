from django.shortcuts import render
from .models import Usuarios
from .forms import CreateUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def loginUsers(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "HistoryBattlesApp/home.html")
        else:
            return render(request, "login/login.html", {'error':'Usuario o contraseña incorrectos'})
    else:
        return render(request, "login/login.html")


def register(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, "login/login.html")
    else:
        return render(request, "register/register.html")

