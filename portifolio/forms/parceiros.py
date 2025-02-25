from core.forms import BaseForm
from portifolio.models import Parceiros


class ParceirosForm(BaseForm):
    """Form padrão para o model Parceiros"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Parceiros
