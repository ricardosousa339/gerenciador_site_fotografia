from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import ImagemGenerica


class ImagemGenericaSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagemGenerica para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = ImagemGenerica
        exclude = ["deleted", "enabled"]
