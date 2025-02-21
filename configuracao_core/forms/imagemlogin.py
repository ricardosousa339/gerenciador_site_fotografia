from configuracao_core.models import ImagemLogin
from core.forms import BaseForm


class ImagemLoginForm(BaseForm):
    """Form padrão para o model ImagemLogin"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = ImagemLogin
