from core.forms import BaseForm
from portifolio.models import Categoria


class CategoriaForm(BaseForm):
    """Form padrão para o model Categoria"""

    class Meta:
        exclude = ["deleted", "enabled", "usuario"]
        model = Categoria


class CategoriaModalForm(CategoriaForm): ...
