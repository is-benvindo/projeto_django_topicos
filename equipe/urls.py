from django.urls import path
from . import views

app_name = "equipe"

urlpatterns = [
    path('relatorios/', views.listar_equipes, name='listar_equipes'),
    path('detalhes/<int:id>/', views.detalhes_equipe, name='detalhes_equipe'),  # Para ver detalhes de uma equipe específica
]
