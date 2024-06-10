from django.db import models
import datetime


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, null = True)
    ano_formacao = models.PositiveIntegerField(null = True)

    pais_origem = models.CharField(max_length=100,null = True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albums')

    #lancamento = models.DateField(default=datetime.date.today().strftime('%d-%m-%Y'))

    gravadora = models.CharField(max_length=100, null=True)
    capa_album = models.ImageField(null=True)

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')

    duracao = models.PositiveIntegerField(null = True)

    numero_faixa = models.PositiveIntegerField(null = True)

    def __str__(self):
        return self.titulo

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='membros')
    papel_na_banda = models.CharField(max_length=100,null = True)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='comentarios')

    #data_publicacao = models.DateField(default=datetime.date.today().strftime('%d-%m-%Y'))

    def __str__(self):
        return f"{self.autor} - {self.album}"
