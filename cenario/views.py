from django.shortcuts import render
from .models import Cenario
from ambiente.models import Ambiente, Decisao, Participante, Atividade

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

def cenario(request, id=0, versao=0):
    versao_carregada = versao
    cenario = Cenario.objects.get(id=id)
    ambiente = Ambiente.objects.get(id=cenario.ambiente.id)
    atividades = Atividade.objects.filter(ambiente=ambiente, versao=versao)

    versoes = Atividade.objects.filter(ambiente=ambiente).order_by('-versao')
    versoes_atividades = {}
    
    for versao in versoes:
        versoes_atividades.update({versao.versao: 0})

    for versao in versoes:
        versoes_atividades[versao.versao] = versoes_atividades[versao.versao] + 1

    dados = {
        'cenario': cenario,
        'ambiente': cenario.ambiente.id,
        'atividades': atividades,
        'versoes': versoes_atividades,
        'versao_carregada': versao_carregada,
        'tipo_ambiente': ambiente.predefinicao.nome
    }

    print(dados)

    return render(request, 'cenario/cenario.html', dados)