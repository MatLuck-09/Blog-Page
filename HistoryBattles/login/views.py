from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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
    try:
        if request.method == "POST":
            userCreate = UserCreationForm(request.POST)
            if userCreate is not None:
                userCreate.save()
                return redirect("../")
        else:
            return render(request, "register/register.html")
    except:
        messages.error(request, "Ocurrió un error durante el registro. Por favor, inténtalo nuevamente.")

    return redirect("register:register")
