from django.contrib import admin
from .models import Modalidade, Atleta, Tecnico, Equipe

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'modalidade', 'matricula')
    search_fields = ('nome_completo', 'matricula')
    list_filter = ('modalidade',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'modalidade', 'cpf', 'funcao')  # Removi matrícula e adicionei função
    search_fields = ('nome', 'cpf')
    list_filter = ('modalidade', 'funcao')  # Adicionei filtro de função

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_time', 'modalidade', 'tecnico')
    search_fields = ('nome_time',)
    list_filter = ('modalidade',)

# Personalização do Admin
admin.site.site_header = 'Cadastro de Times - IFPI'
admin.site.site_title = 'Cadastro de Times - IFPI'
admin.site.index_title = 'Painel de Administração'