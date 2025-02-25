from core.forms import BaseForm
from portifolio.models import SecaoSobre


class SecaoSobreForm(BaseForm):
    """Form padrão para o model SecaoSobre"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = SecaoSobre


class SecaoSobreModalForm(SecaoSobreForm): ...
