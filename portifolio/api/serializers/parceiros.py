from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import Parceiros


class ParceirosSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Parceiros para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Parceiros
        exclude = ["deleted", "enabled"]
