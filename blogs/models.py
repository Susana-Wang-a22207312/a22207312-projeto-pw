from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor_nome = models.CharField(max_length=100)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f"Comentário por {self.autor_nome} em {self.artigo.titulo}:"

class Rating(models.Model):
    autor_nome = models.CharField(max_length=100)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"Classificação de {self.autor_nome} para {self.artigo.titulo}: {self.rating}"
