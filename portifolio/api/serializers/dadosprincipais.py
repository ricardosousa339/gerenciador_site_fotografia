from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import DadosPrincipais


class DadosPrincipaisSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model DadosPrincipais para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = DadosPrincipais
        exclude = ["deleted", "enabled"]
