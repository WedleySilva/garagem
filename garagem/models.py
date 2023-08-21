from django.db import models
from uploader.models import Image

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()    

    class Meta:
        verbose_name = "acessório"
        verbose_name_plural = "acessórios"


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()    

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nome.upper()                                 

class Modelo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()   

class Veiculo(models.Model):
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")
    ano = models.DateField(max_length=4)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="veiculos",
    )
    cor =models.ForeignKey(
        Cor, on_delete=models.CASCADE, related_name="veiculos",
        )
   
    marca = models.ForeignKey(
        Marca, on_delete=models.CASCADE, related_name="veiculos",
    )
    
    modelo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
       
    )
    modelo = ImageSerializer(required=False)

def __str__(self):
        return f"{self.ano} - {self.marca} - {self.modelo} - {self.cor} - {self.categoria} - {self.preco}"





