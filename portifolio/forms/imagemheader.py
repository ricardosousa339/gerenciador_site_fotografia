from core.forms import BaseForm
from portifolio.models import ImagemHeader


class ImagemHeaderForm(BaseForm):
    """Form padrão para o model ImagemHeader"""

    class Meta:
        exclude = ["deleted", "enabled", "usuario"]
        model = ImagemHeader
