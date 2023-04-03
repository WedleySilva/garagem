from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    Cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.marca.modelo.ano.cor
