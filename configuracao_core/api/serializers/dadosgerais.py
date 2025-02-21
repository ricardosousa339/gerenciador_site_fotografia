from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import DadosGerais


class DadosGeraisSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model DadosGerais para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = DadosGerais
        exclude = ["deleted", "enabled"]
