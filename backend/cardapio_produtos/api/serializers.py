from rest_framework.serializers import ModelSerializer
from backend.cardapio_produtos.models import CardapioProduto
from backend.cafes.api.serializers import CafesSerializers
from backend.doces.api.serializers import DocesSerializers
from backend.salgados.api.serializers import SalgadosSerializers
from backend.chas.api.serializers import ChasSerializers
from backend.bebidas.api.serializers import BebidasSerializers

class CardapioPodutoSerializers(ModelSerializer):
    # acessa os dados de uma chave estrangeira por meio de serializers,
    # unindo json
    cafes = CafesSerializers(many=True, read_only=True)
    doces = DocesSerializers(many=True, read_only=True)
    salgados = SalgadosSerializers(many=True, read_only=True)
    chas = ChasSerializers(many=True, read_only=True)
    bebidas = BebidasSerializers(many=True, read_only=True)

    class Meta:
        model = CardapioProduto
        fields = ('id', 'nome', 'cafes', 'doces', 'salgados', 'chas', 'bebidas')