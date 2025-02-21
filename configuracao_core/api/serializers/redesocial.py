from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from configuracao_core.models import RedeSocial


class RedeSocialSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model RedeSocial para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = RedeSocial
        exclude = ["deleted", "enabled"]
