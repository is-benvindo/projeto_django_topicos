from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # Rota para o Django Admin
    path("equipe/", include("equipe.urls", namespace="equipe")),  # Inclui URLs do app 'equipe'
    # Caso tenha mais apps, basta adicionar outra linha seguindo o mesmo padrão.
]

# Configuração para servir arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)