from rest_framework.serializers import ModelSerializer
from backend.cafes.models import Cafes

class CafesSerializers(ModelSerializer):
    class Meta:
        model = Cafes
        fields = ('id', 'nome', 'descricao', 'ml', 'preco', 'foto_cafe')

