from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import LogoSistema


class LogoSistemaSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model LogoSistema para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = LogoSistema
        exclude = ["deleted", "enabled"]
