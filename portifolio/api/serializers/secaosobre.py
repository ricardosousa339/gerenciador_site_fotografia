from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import SecaoSobre


class SecaoSobreSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model SecaoSobre para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = SecaoSobre
        exclude = ["deleted", "enabled"]
