from django.db import models

# Create your models here.


    


class Projetos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    repositorio = models.CharField(max_length=100)
    conceitos = models.CharField(max_length=500)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    site = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    
class UC(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    docente = models.ManyToManyField(Docente, related_name="ucs")
    imagem = models.ImageField(upload_to="fotos_uc/", blank=True)

    def __str__(self):
        return self.nome



class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    uc = models.ManyToManyField(UC, related_name="licenciaturas", blank=True)

    def __str__(self):
        return self.nome
