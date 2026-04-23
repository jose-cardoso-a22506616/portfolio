from django.db import models

# Create your models here.

class Tfc(models.Model):
    titulo = models.CharField(max_length=100)
    aluno = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    licenciatura = models.CharField(max_length=100)
    pdf = models.URLField()
    email = models.EmailField()
    resumo = models.TextField()
    palavras_chave = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    tecnologias = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.titulo



class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    fotos = models.ImageField(upload_to="fotos_makingof/", blank=True)
    descricao = models.TextField(blank=True)
    alteracao = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)
    llm = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.titulo



class Formacao(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"{self.tipo} feito em {self.data}"



class Competencia(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.tipo



class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    site_oficial = models.URLField(blank=True)
    descricao = models.TextField()
    logo = models.ImageField(upload_to="fotos_tecnologia/", blank=True)
    classificacao = models.IntegerField()
    formacao = models.ManyToManyField(Formacao, related_name="tecnologias", blank=True)

    def __str__(self):
        return f"Tecnologia: {self.nome} | Classificação: {self.classificacao}/5"
    
    
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    card_code = models.IntegerField()
    employee_code = models.IntegerField()
    degree = models.CharField(max_length=25, blank=True, null=True)
    regime = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

    
class UC(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    objetivo = models.TextField(blank=True)
    programa = models.TextField(blank=True)

    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()

    docente = models.ManyToManyField(Docente, related_name="ucs", blank=True)
    imagem = models.ImageField(upload_to="fotos_uc/", blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    repositorio = models.CharField(max_length=100, blank=True)
    conceitos = models.CharField(max_length=500)
    tecnologia = models.ManyToManyField(Tecnologia, related_name="projetos")
    competencia = models.ManyToManyField(Competencia, related_name="projetos")
    
    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name="projetos", blank=True, null=True)

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    curso_codigo = models.IntegerField()
    semestres = models.IntegerField()
    descricao = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    curso_ects = models.IntegerField()
    uc = models.ManyToManyField(UC, related_name="licenciaturas", blank=True)

    def __str__(self):
        return self.nome
