from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from usuario.models import Usuario


class UsuarioSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Usuario para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Usuario
        exclude = ["deleted", "enabled"]
