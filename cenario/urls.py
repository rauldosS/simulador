from django.urls import include, path
from . import views

app_name = 'cenario'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cenario/<int:id>', views.cenario, name='cenario'),
    # path('salvar_cenario/', views.salvarCenario, name='salvar_cenario'),
]