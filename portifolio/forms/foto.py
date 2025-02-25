from core.forms import BaseForm
from portifolio.models import Foto


class FotoForm(BaseForm):
    """Form padrão para o model Foto"""

    class Meta:
        exclude = ["deleted", "enabled", "usuario"]
        model = Foto


class FotoModalForm(FotoForm): ...
