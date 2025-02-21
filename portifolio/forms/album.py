from core.forms import BaseForm
from portifolio.models import Album


class AlbumForm(BaseForm):
    """Form padrão para o model Album"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Album


class AlbumModalForm(AlbumForm): ...
