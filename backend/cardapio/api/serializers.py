from rest_framework.serializers import ModelSerializer
from backend.cardapio.models import Cardapio
from backend.cafes.api.serializers import CafesSerializers
from backend.doces.api.serializers import DocesSerializers
from backend.salgados.api.serializers import SalgadosSerializers

class CardapioSerializers(ModelSerializer):
    # acessa os dados de uma chave estrangeira por meio de serializers,
    # unindo json
    cafes = CafesSerializers()
    doces = DocesSerializers()
    salgados = SalgadosSerializers()

    class Meta:
        model = Cardapio
        fields = ('id', 'nome', 'cafes', 'doces', 'salgados')