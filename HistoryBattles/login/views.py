from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from .forms import CustomUserCreationForm , UserCreationForm
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


<<<<<<< HEAD
def register(request):
    if request.method == 'POST':
        form2 = UserCreationForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('../')
=======
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('/')
>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo "{field}": {error}')
    else:
        form2 = UserCreationForm()
    
<<<<<<< HEAD
    return render(request, 'register/register.html', {'form': form2})
=======
    return render(request, 'register/register.html', {'form': form})



>>>>>>> c2415f5749d574ffd48becf5b61d1308080324ba
