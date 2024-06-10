from django.db import models

class AreaCientifica(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    curricularUnitReadableCode = models.CharField(max_length=100)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(null=True)
    video_demo = models.URLField(max_length=200)
    github_repo = models.URLField(max_length=200)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE, related_name='projeto')

    def __str__(self):
        return f"Projeto de {self.disciplina.nome}"

class LinguagemProgramacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina, related_name='docentes')

    def __str__(self):
        return self.nome

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    disciplinas = models.ManyToManyField(Disciplina, related_name='cursos')

    def __str__(self):
        return "Curso"
