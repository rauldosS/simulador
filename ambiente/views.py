from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ambiente, Opcao
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Count
import json

# Create your views here.
def inicio(request):
    ambientes = Ambiente.objects.all()

    dados = {
        'ambientes': ambientes
    }

    return render(request, 'ambiente/inicio.html', dados)

def ambiente(request, id=0, versao=0):
    versao_carregada = versao
    ambiente = Ambiente.objects.get(id=id)
    opcoes = Opcao.objects.filter(ambiente=ambiente, versao=versao)

    versoes = Opcao.objects.filter(ambiente=ambiente).order_by('-versao')
    versoes_opcoes = {}
    
    for versao in versoes:
        versoes_opcoes.update({versao.versao: 0})

    for versao in versoes:
        versoes_opcoes[versao.versao] = versoes_opcoes[versao.versao] + 1

    dados = {
        'ambiente': ambiente,
        'opcoes': opcoes,
        'versoes': versoes_opcoes,
        'versao_carregada': versao_carregada
    }

    return render(request, 'ambiente/ambiente.html', dados)

def salvarAmbiente(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.POST.get('dados', ''))
            
            ambiente = Ambiente.objects.get(id=dados['ambiente'])
            ambiente.versao = ambiente.versao + 1
            ambiente.save()

            atualizarOpcoes(ambiente, dados['opcoes'])

            return JsonResponse({'versao': ambiente.versao})
        except Exception as e:
            print(e)
            return JsonResponse({'erro': 'erro'})

def atualizarOpcoes(ambiente, opcoes):
    for opcao, dados in opcoes.items():
        registrarOpcao(ambiente, opcao, dados, ambiente.versao)

def registrarOpcao(ambiente, opcao, dados, versao):
    op = Opcao.objects.create(
        ambiente=ambiente,
        opcao=opcao,
        nome=dados['nome'],
        direcao=dados['direcao'],
        duracao=int(dados['duracao']),
        tipo=dados['tipo'],
        versao=versao,
    )

    op.save()