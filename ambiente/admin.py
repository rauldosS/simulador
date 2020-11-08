from django.contrib import admin
from ambiente.models import Ambiente, Opcao, Decisao, Participante

# Register your models here.
@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data']
    list_filter = ['data']
    search_filter = ['nome']

@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ambiente', 'opcao', 'direcao', 'duracao']
    list_filter = ['ambiente']
    search_filter = ['ambiente', 'opcao']

@admin.register(Decisao)
class DecisaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'opcao', 'formula']
    list_filter = ['opcao', 'formula']
    search_filter = ['opcao', 'formula']

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'ambiente', 'nome', 'idade', 'sexo']
    list_filter = ['ambiente', 'nome']
    search_filter = ['ambiente', 'nome', 'idade', 'sexo']