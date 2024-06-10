from django.db import models

class Regiao(models.Model):
    distrito = models.CharField(max_length=200)
    concelho = models.CharField(max_length=200)

    def __str__(self):
        return self.distrito

class Praia(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey('Regiao', on_delete=models.CASCADE)
    # imagem = models.ImageField(upload_to='praia_images/')

    def __str__(self):
        return self.nome

class Servico(models.Model):
    tipo_servico = models.CharField(max_length=100)
    custo = models.IntegerField()
    praias = models.ManyToManyField('Praia', related_name='servicos', null = True)

    def __str__(self):
        return self.tipo_servico
