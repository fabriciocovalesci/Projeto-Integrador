from rest_framework.serializers import ModelSerializer
from backend.fotosfrontend.models import FotosFrontend

class FotosFrontendSerializers(ModelSerializer):
    class Meta:
        model = FotosFrontend
        fields = ('id', 'foto_frontend')