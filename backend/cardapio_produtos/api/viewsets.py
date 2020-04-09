from rest_framework.viewsets import ModelViewSet
from backend.cardapio_produtos.models import CardapioProduto
from .serializers import CardapioPodutoSerializers

class CardapioProdutoViewSets(ModelViewSet):
    queryset = CardapioProduto.objects.all()
    serializer_class = CardapioPodutoSerializers
