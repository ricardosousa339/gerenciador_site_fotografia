from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import FatoSobre


class FatoSobreSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model FatoSobre para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = FatoSobre
        exclude = ["deleted", "enabled"]
