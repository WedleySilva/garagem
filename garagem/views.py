from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Veiculo, Acessorio, Cor, Marca, Modelo
from garagem.serializers import CategoriaSerializer, VeiculoSerializer, AcessorioSerializer, CorSerializer, MarcaSerializer, ModeloSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer  

class CorViewSet(ModelViewSet):         
    queryset = Cor.objects.all()
    serializer_class = CorSerializer    

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer



