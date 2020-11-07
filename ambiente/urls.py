from django.urls import include, path
from . import views

app_name = 'ambiente'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ambiente/<int:id>', views.ambiente, name='ambiente')
]