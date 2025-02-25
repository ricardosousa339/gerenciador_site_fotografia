from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import MensagemContato


class MensagemContatoSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model MensagemContato para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = MensagemContato
        exclude = ["deleted", "enabled"]
