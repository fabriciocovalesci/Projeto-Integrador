from rest_framework.viewsets import ModelViewSet
from backend.usuario.models import Usuario
from .serializers import UsuarioSerializers


class UsuarioViewSets(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
