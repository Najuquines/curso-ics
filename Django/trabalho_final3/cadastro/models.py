from django.db import models

class Cadastro(models.Model):
    primeiro_e_ultimo_nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    cidade_e_estado = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
  

    def __str__ (self):
      return self.primeiro_e_ultimo_nome
