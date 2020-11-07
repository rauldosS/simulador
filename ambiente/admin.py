from django.contrib import admin
from ambiente.models import Ambiente

# Register your models here.
@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data']
    list_filter = ['data']
    search_filter = ['nome']