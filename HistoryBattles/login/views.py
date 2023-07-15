from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        form2 = UserCreationForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('../')
        else:
            for field, errors in form2.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo "{field}": {error}')
    else:
        form2 = UserCreationForm()
    
    return render(request, 'register/register.html', {'form': form2})
