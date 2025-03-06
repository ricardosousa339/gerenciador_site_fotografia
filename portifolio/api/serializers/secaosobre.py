from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.api.serializers.foto import FotoSerializer
from portifolio.models import SecaoSobre


class SecaoSobreSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model SecaoSobre para o POST, PUT, PATCH, DELETE"""
    imagem = FotoSerializer(many=False, read_only=True)
    class Meta:
        model = SecaoSobre
        exclude = ["deleted", "enabled"]
