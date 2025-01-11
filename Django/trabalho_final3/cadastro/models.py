from django.db import models

class Cadastr(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
  

def __str__ (self):
    return self.nome
