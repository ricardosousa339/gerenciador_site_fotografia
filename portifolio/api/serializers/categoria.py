from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import Categoria


class CategoriaSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Categoria para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Categoria
        exclude = ["deleted", "enabled"]
