from rest_framework.viewsets import ModelViewSet
from .serializers import FotosFrontendSerializers
from backend.fotosfrontend.models import FotosFrontend

class FotosFrontendViewSets(ModelViewSet):
    queryset = FotosFrontend.objects.all()
    serializer_class = FotosFrontendSerializers