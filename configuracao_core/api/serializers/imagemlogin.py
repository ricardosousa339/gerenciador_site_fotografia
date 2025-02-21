from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import ImagemLogin


class ImagemLoginSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagemLogin para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = ImagemLogin
        exclude = ["deleted", "enabled"]
