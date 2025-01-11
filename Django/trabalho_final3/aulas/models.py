from django.db import models

class Aulas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)  

    def __str__ (self):
        return self.titulo


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    aulas = models.ManyToManyField(Aulas)
    imagem = models.CharField(max_length=1000)

    def __str__ (self):
        return self.nome
