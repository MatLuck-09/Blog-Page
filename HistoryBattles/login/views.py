from django.shortcuts import render
from .models import Usuarios
from .forms import CreateUser

# Create your views here.
def login(request):
    if request.method == 'POST':
        forms = CreateUser(request.POST)
        if forms.is_valid():
            data = forms.cleaned_data
            user = Usuarios(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])
            user.save()
        return render(request, "HistoryBattlesApp/home.html")
    else:
        form = CreateUser()

    return render(request, "login/login.html", {'form': form})
