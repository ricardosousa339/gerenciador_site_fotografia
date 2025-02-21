from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import ImagensSistema


class ImagensSistemaSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagensSistema para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = ImagensSistema
        exclude = ["deleted", "enabled"]
