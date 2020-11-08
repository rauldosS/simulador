from django.shortcuts import render, redirect
from .models import Ambiente, Opcao
from django.http import HttpResponseRedirect, JsonResponse
import json

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

def salvarAmbiente(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.POST.get('dados', ''))
            
            ambiente = Ambiente.objects.get(id=dados['ambiente'])

            atualizarOpcoes(ambiente, dados['opcoes'])

            return JsonResponse({'ok': 'ok'}) 
        except Exception as e:
            print(e)
            return JsonResponse({'erro': 'erro'})

def atualizarOpcoes(ambiente, opcoes):
    for opcao, dados in opcoes.items():
        
        try:
            objeto_opcao = Opcao.objects.get(ambiente=ambiente, opcao=str(opcao))
            print(objeto_opcao)

            atualizarOpcao(objeto_opcao, dados)
        except Exception as e:
            registrarOpcao(ambiente, opcao, dados)

def atualizarOpcao(opcao, dados):
    opcao.nome=dados['nome']
    opcao.direcao=dados['direcao']
    opcao.duracao=int(dados['duracao'])
    opcao.tipo=dados['tipo']

    opcao.save()

def registrarOpcao(ambiente, opcao, dados):
    op = Opcao.objects.create(
        ambiente=ambiente,
        opcao=opcao,
        nome=dados['nome'],
        direcao=dados['direcao'],
        duracao=int(dados['duracao']),
        tipo=dados['tipo'],
    )

    op.save()

