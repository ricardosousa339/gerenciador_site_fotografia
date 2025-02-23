from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import ImagemHeader


class ImagemHeaderSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagemHeader para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = ImagemHeader
        exclude = ["deleted", "enabled"]
