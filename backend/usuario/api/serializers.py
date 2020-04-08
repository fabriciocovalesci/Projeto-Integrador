from rest_framework.serializers import ModelSerializer
from backend.usuario.models import Usuario


class UsuarioSerializers(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'telefone', 'data_nascimento', 'endereco', 'foto_usuario')
