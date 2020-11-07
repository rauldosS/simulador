from django.shortcuts import render
from .models import Ambiente

# Create your views here.
def inicio(request):
    ambientes = Ambiente.objects.all()

    dados = {
        'ambientes': ambientes
    }

    return render(request, 'ambiente/inicio.html', dados)

def ambiente(request, id=0):
    ambiente = Ambiente.objects.get(id=id)

    dados = {
        'ambiente': ambiente
    }

    return render(request, 'ambiente/ambiente.html', dados)