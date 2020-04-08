from rest_framework.viewsets import ModelViewSet
from .serializers import ChasSerializers
from backend.chas.models import Chas

class ChasViewSets(ModelViewSet):
    queryset = Chas.objects.all()
    serializer_class = ChasSerializers