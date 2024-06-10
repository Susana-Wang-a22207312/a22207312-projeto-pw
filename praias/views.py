from django.shortcuts import render
from .models import Regiao, Praia, Servico


def index_view(request):
    context = {
        'regioes': Regiao.objects.all().order_by('distrito'),
    }
    return render(request, "praias/index.html",context)


def praia_view(request, praia_nome):
    context = {
      'praia': Praia.objects.get(nome=praia_nome),
   }
    return render(request, "praias/praia.html",context)



