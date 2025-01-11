from django.db import models

class Aulas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    cursos = models.CharField(max_length=100)
  

def __str__ (self):
    return self.nome

