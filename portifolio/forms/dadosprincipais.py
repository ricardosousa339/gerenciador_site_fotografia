from core.forms import BaseForm
from portifolio.models import DadosPrincipais


class DadosPrincipaisForm(BaseForm):
    """Form padrão para o model DadosPrincipais"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = DadosPrincipais
