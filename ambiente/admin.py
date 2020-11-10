from django.contrib import admin
from ambiente.models import Ambiente, Opcao, Decisao, Participante, PredefinicaoSimulacao

# Register your models here.
@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data', 'versao']
    list_filter = ['data']
    search_filter = ['nome']

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ambiente', 'opcao', 'direcao', 'duracao', 'versao']
    list_filter = ['ambiente', 'versao']
    search_filter = ['ambiente', 'opcao', 'versao']

@admin.register(Decisao)
class DecisaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'opcao', 'formula']
    list_filter = ['opcao', 'formula']
    search_filter = ['opcao', 'formula']

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'ambiente', 'nome']
    list_filter = ['ambiente', 'nome']
    search_filter = ['ambiente', 'nome']

@admin.register(PredefinicaoSimulacao)
class PredefinicaoSimulacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_filter = ['nome']