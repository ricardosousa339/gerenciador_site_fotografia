from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import SecaoContato


class SecaoContatoSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model SecaoContato para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = SecaoContato
        exclude = ["deleted", "enabled"]
