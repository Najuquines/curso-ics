from django.db import models

class Aulas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)  
    link = models.CharField(max_length=200)
    
    def __str__ (self):
        return self.titulo


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    aulas = models.ManyToManyField(Aulas)
    imagem = models.CharField(max_length=1000)
    material_escrito = models.CharField(max_length=100, null=True, blank=True)

    def __str__ (self):
        return self.nome
