from drf_jsonmask.serializers import FieldsListSerializerMixin
from rest_framework.serializers import ModelSerializer

from portifolio.models import Album


class AlbumSerializer(FieldsListSerializerMixin, ModelSerializer):
    """Class do serializer do model Album para o POST, PUT, PATCH, DELETE"""

    class Meta:
        model = Album
        exclude = ["deleted", "enabled"]
