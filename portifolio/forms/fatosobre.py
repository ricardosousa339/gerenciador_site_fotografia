from core.forms import BaseForm
from portifolio.models import FatoSobre


class FatoSobreForm(BaseForm):
    """Form padrão para o model FatoSobre"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = FatoSobre
