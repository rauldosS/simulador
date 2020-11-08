from django.urls import include, path
from . import views

app_name = 'ambiente'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ambiente/<int:id>/<int:versao>', views.ambiente, name='ambiente'),
    path('salvar_ambiente/', views.salvarAmbiente, name='salvar_ambiente'),
]