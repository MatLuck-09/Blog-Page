from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from perfil.views import getAvatar

# Create your views here.
@login_required
def home(request):
    avatar = getAvatar(request)

    return render(request, "HistoryBattlesApp/home.html", {"avatar":avatar})