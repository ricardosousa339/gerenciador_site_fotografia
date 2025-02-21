from configuracao_core.models import RedeSocial
from core.forms import BaseForm


class RedeSocialForm(BaseForm):
    """Form padrão para o model RedeSocial"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = RedeSocial
