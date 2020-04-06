from rest_framework.viewsets import ModelViewSet
from backend.salgados.models import Salgados
from .serializers import SalgadosSerializers

class SalgadosViewSets(ModelViewSet):
    queryset = Salgados.objects.all()
    serializer_class = SalgadosSerializers