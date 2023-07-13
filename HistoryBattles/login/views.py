from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate 
from django.http import HttpResponseServerError

def loginUsers(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "HistoryBattlesApp/home.html")
        else:
            return render(request, "login/login.html", {'error1':'Usuario o contraseña incorrectos'})
    else:
        return render(request, "login/login.html")


def register(request):
    try:
        if request.method == "POST":
            userCreate = UserCreationForm(request.POST)
            if userCreate.is_valid():
                userCreate.save()
                return redirect("../")
        else:
            return render(request, "register/register.html")
    except:
        return HttpResponseServerError('Contraseña demasiado corta (mayor a 8 caracteres), recuerda que tambien puedes utilizar numeros y letras.')

    return redirect("register:register")
