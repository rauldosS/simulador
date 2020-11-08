from django.shortcuts import render
from .models import Cenario
from ambiente.models import Ambiente, Opcao, Decisao, Participante

# Create your views here.
def inicio(request):
    ambientes = Ambiente.objects.all()
    
    cenarios_ambientes = {}

    for ambiente in ambientes:
        cenarios_ambientes.update( { ambiente.id: {'cenarios': {}} } )
        cenarios_ambientes[ambiente.id].update( { 'nome': str(ambiente.nome) } )

    for ambiente in ambientes:
        cenarios = Cenario.objects.filter(ambiente=ambiente)

        for cenario in cenarios:
            cenarios_ambientes[ambiente.id]['cenarios'].update({
                cenario.id: str(cenario.nome)
            })

    dados = {
        'cenarios_ambientes': cenarios_ambientes
    }

    return render(request, 'cenario/inicio.html', dados)

def cenario(request, id):
    cenario = Cenario.objects.get(id=id)

    dados = {
        'cenario': cenario
    }

    return render(request, 'cenario/cenario.html', dados)