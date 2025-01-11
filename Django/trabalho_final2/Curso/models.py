from django.db import models


class Dados_pessoais(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

def __str__ (self):
    return self.nome

