from configuracao_core.models import ImagemGenerica
from core.forms import BaseForm


class ImagemGenericaForm(BaseForm):
    """Form padrão para o model ImagemGenerica"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = ImagemGenerica


class ImagemGenericaModalForm(ImagemGenericaForm): ...
