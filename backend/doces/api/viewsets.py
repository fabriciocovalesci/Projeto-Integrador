from rest_framework.viewsets import ModelViewSet
from backend.doces.models import Doces
from .serializers import DocesSerializers

class DocesViewSets(ModelViewSet):
    queryset = Doces.objects.all()
    serializer_class = DocesSerializers