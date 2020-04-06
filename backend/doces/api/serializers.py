from rest_framework.serializers import ModelSerializer
from backend.doces.models import Doces

class DocesSerializers(ModelSerializer):
    class Meta:
        model = Doces
        fields = ('id', 'nome', 'descricao', 'unidades', 'preco', 'foto_doces')