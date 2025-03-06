from drf_jsonmask.serializers import FieldsListSerializerMixin
from portifolio.api.serializers.foto import FotoSerializer
from rest_framework.serializers import ModelSerializer

from portifolio.models import ImagemHeader


class ImagemHeaderSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model ImagemHeader para o POST, PUT, PATCH, DELETE"""
    imagem = FotoSerializer(many=False, read_only=True)

    class Meta:
        model = ImagemHeader
        exclude = ["deleted", "enabled"]
