from django.db import models

# Create your models here.
class Planos(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.IntegerField()
    repositorios = models.IntegerField()
    membros = models.IntegerField()
    tamanho = models.CharField(max_length=30)
    suporte = models.BooleanField(default=False)