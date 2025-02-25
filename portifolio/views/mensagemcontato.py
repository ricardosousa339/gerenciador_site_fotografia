from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.mensagemcontato import MensagemContatoForm
from portifolio.models import MensagemContato


# Views do Models MensagemContato
class MensagemContatoListView(BaseListView):
    """Classe para gerenciar a listagem do MensagemContato"""

    model = MensagemContato
    template_name = "portifolio/mensagemcontato/mensagemcontato_list.html"
    context_object_name = "mensagemcontato"
    list_display = ["email", "nome"]
    search_fields = ["email", "nome"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MensagemContatoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(MensagemContatoListView, self).get_queryset()
        return queryset


class MensagemContatoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do MensagemContato"""

    model = MensagemContato
    form_class = MensagemContatoForm
    success_url = "portifolio:mensagemcontato-list"
    template_name = "portifolio/mensagemcontato/mensagemcontato_detail.html"
    context_object_name = "mensagemcontato"

    def get_context_data(self, **kwargs):
        context = super(MensagemContatoDetailView, self).get_context_data(**kwargs)
        return context


class MensagemContatoCreateView(BaseCreateView):
    """Classe para gerenciar o create do MensagemContato"""

    model = MensagemContato
    form_class = MensagemContatoForm
    context_object_name = "mensagemcontato"
    success_url = "portifolio:mensagemcontato-list"
    template_name = "portifolio/mensagemcontato/mensagemcontato_create.html"
    # inlines = []
    # form_modals = []


class MensagemContatoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do MensagemContato"""

    model = MensagemContato
    form_class = MensagemContatoForm
    context_object_name = "mensagemcontato"
    success_url = "portifolio:mensagemcontato-list"
    template_name = "portifolio/mensagemcontato/mensagemcontato_update.html"
    # inlines = []
    # form_modals = []


class MensagemContatoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do MensagemContato"""

    model = MensagemContato
    form_class = MensagemContatoForm
    context_object_name = "mensagemcontato"
    success_url = "portifolio:mensagemcontato-list"
    template_name = "portifolio/mensagemcontato/mensagemcontato_delete.html"


class MensagemContatoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do MensagemContato"""

    model = MensagemContato
    context_object_name = "mensagemcontato"
    success_url = "portifolio:mensagemcontato-list"
    template_name = "portifolio/mensagemcontato/mensagemcontato_restore.html"


# Fim das Views do Models MensagemContato
