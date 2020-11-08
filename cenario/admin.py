from django.contrib import admin
from .models import Cenario

# Register your models here.
@admin.register(Cenario)
class CenarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ambiente']
    list_filter = ['ambiente']
    search_filter = ['nome', 'ambiente']