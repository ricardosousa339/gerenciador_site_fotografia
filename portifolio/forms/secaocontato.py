from core.forms import BaseForm
from portifolio.models import SecaoContato


class SecaoContatoForm(BaseForm):
    """Form padrão para o model SecaoContato"""

    class Meta:
        exclude = ["deleted", "enabled", "usuario"]
        model = SecaoContato
