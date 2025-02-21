from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import Gestor


class GestorSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Gestor para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Gestor
        exclude = ["deleted", "enabled"]
