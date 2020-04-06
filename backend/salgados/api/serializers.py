from rest_framework.serializers import ModelSerializer
from backend.salgados.models import Salgados

class SalgadosSerializers(ModelSerializer):
    class Meta:
        model = Salgados
        fields = ('id', 'nome', 'descricao', 'unidades', 'preco', 'foto_salgados')