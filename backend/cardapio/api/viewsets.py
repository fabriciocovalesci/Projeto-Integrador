from rest_framework.viewsets import ModelViewSet
from backend.cardapio.models import Cardapio
from .serializers import CardapioSerializers

class CardapioViewSets(ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializers