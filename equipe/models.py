from django.db import models
from django.core.validators import RegexValidator

# Modelo de Modalidade
class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

# Modelo de Atleta
class Atleta(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20, unique=True)
    comprovante_matricula = models.FileField(upload_to='comprovantes_matricula/', blank=True)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_completo

# Modelo de Técnico
class Tecnico(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(
        max_length=14,
        unique=True
    )
    funcao = models.CharField(
        max_length=50,
        choices=[
            ('professor', 'Professor'),
            ('coordenador', 'Coordenador'),
            ('assistente', 'Assistente')
        ],
        default='professor'
    )
    modalidade = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

# Modelo de Equipe
class Equipe(models.Model):
    nome_time = models.CharField(max_length=255, unique=True)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)  # Cada equipe terá um técnico
    atletas = models.ManyToManyField(Atleta, blank=True)  # Muitos atletas podem estar em uma equipe

    def __str__(self):
        return self.nome_time
