from rest_framework.viewsets import ModelViewSet
from backend.cafes.models import Cafes
from .serializers import CafesSerializers

class CafesViewSets(ModelViewSet):
    queryset = Cafes.objects.all()
    serializer_class = CafesSerializers



