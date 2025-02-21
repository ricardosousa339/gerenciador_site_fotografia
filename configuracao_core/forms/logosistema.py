from configuracao_core.models import LogoSistema
from core.forms import BaseForm


class LogoSistemaForm(BaseForm):
    """Form padrão para o model LogoSistema"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = LogoSistema
