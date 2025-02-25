from core.forms import BaseForm
from portifolio.models import MensagemContato


class MensagemContatoForm(BaseForm):
    """Form padrão para o model MensagemContato"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = MensagemContato
