from django.shortcuts import render
from .models import Equipe

def listar_equipes(request):
    equipes = Equipe.objects.select_related('tecnico', 'modalidade').prefetch_related('atletas').all()  # Removido 'medicos'
    return render(request, 'equipe/listar_equipes.html', {'equipes': equipes})