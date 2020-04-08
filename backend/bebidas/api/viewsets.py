from rest_framework.viewsets import ModelViewSet
from .serializers import BebidasSerializers
from backend.bebidas.models import Bebidas


class BebidasViewSets(ModelViewSet):
    queryset = Bebidas.objects.all()
    serializer_class = BebidasSerializers