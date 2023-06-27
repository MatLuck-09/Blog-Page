from django.shortcuts import render
from battles.models import Batalla, EjercitoVencedor, EjercitoVencido

# Create your views here.
def battles(request):

    batallas = Batalla.objects.all()
    ejercito1 = EjercitoVencedor.objects.all()
    ejercito2 = EjercitoVencido.objects.all()
    return render(request, "battles/battles.html", {"batallas" : batallas, "ejercito1": ejercito1, "ejercito2": ejercito2})

