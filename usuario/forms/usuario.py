from core.forms import BaseForm
from usuario.models import Usuario


class UsuarioForm(BaseForm):
    """Form padrão para o model Usuario"""

    class Meta:
        exclude = ["deleted", "enabled"]
        model = Usuario
