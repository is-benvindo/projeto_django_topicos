from django.urls import path
from . import views

app_name = "equipe"

urlpatterns = [
    path('relatorios/', views.listar_equipes, name='listar_equipes'),
]
