from rest_framework.serializers import ModelSerializer
from backend.chas.models import Chas

class ChasSerializers(ModelSerializer):
    class Meta:
        model = Chas
        fields = ('id', 'nome', 'descricao', 'ml', 'preco', 'foto_chas')
