from django.db import models

# Create your models here.

class Formacao(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return f"{self.tipo} feito em {self.data}"



class Competencia(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo



class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    site_oficial = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="fotos_tecnologia/", blank=True)
    classificacao = models.IntegerField()
    formacao = models.ManyToManyField(Formacao, related_name="tecnologias", blank=True)

    def __str__(self):
        return f"Tecnologia: {self.nome} | Classificação: {self.classificacao}/5"
    


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    repositorio = models.CharField(max_length=100)
    conceitos = models.CharField(max_length=500)
    tecnologia = models.ManyToManyField(Tecnologia, related_name="projetos")
    competencia = models.ManyToManyField(Competencia, related_name="projetos")

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    mail = models.EmailField()
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
