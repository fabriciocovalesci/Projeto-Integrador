from rest_framework.serializers import ModelSerializer
from backend.bebidas.models import Bebidas


class BebidasSerializers(ModelSerializer):
    class Meta:
        model = Bebidas
        fields = ('id', 'descricao', 'ml', 'preco', 'foto_bebida')
