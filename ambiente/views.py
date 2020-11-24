from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ambiente, Atividade
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
    atividades = Atividade.objects.filter(ambiente=ambiente, versao=versao)

    versoes = Atividade.objects.filter(ambiente=ambiente).order_by('-versao')
    versoes_atividades = {}
    
    for versao in versoes:
        versoes_atividades.update({versao.versao: 0})

    for versao in versoes:
        versoes_atividades[versao.versao] = versoes_atividades[versao.versao] + 1

    dados = {
        'ambiente': ambiente,
        'atividades': atividades,
        'versoes': versoes_atividades,
        'versao_carregada': versao_carregada,
    }

    return render(request, 'ambiente/ambiente.html', dados)

def salvarAmbiente(request):
    if request.method == 'POST':
        dados = json.loads(request.POST.get('dados', ''))

        ambiente = Ambiente.objects.get(id=int(dados['ambiente']))
        ambiente.versao = ambiente.versao + 1
        ambiente.save()

        atualizarAtividades(ambiente, dados['atividades'])

        return JsonResponse({'versao': ambiente.versao})

def atualizarAtividades(ambiente, atividades):
    for atividade, dados in atividades.items():
        print(dados)
        registrarAtividade(ambiente, atividade, dados, ambiente.versao)

def registrarAtividade(ambiente, atividade, dados, versao):
    op = Atividade.objects.create(
        ambiente=ambiente,
        atividade=dados['atividade'],
        proxima_atividade=dados['proxima_atividade'],
        atividade_anterior=dados['atividade_anterior'],
        linha=dados['linha'],
        coluna=dados['coluna'],
        direcao=dados['direcao'],
        duracao=int(dados['duracao']),
        tipo=dados['tipo'],
        icone=dados['icone'],
        versao=versao,
        formula=dados['formula'],
        decisao_verdadeira=dados['decisao_verdadeira'],
        decisao_falsa=dados['decisao_falsa'],
    )

    op.save()