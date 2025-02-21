from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import Foto


class FotoSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Foto para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Foto
        exclude = ["deleted", "enabled"]
