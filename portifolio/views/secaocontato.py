from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.secaocontato import SecaoContatoForm
from portifolio.models import SecaoContato


# Views do Models SecaoContato
class SecaoContatoListView(BaseListView):
    """Classe para gerenciar a listagem do SecaoContato"""

    model = SecaoContato
    template_name = "portifolio/secaocontato/secaocontato_list.html"
    context_object_name = "secaocontato"
    list_display = ["descricao", "titulo"]
    search_fields = ["descricao", "titulo"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SecaoContatoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(SecaoContatoListView, self).get_queryset()
        return queryset


class SecaoContatoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do SecaoContato"""

    model = SecaoContato
    form_class = SecaoContatoForm
    success_url = "portifolio:secaocontato-list"
    template_name = "portifolio/secaocontato/secaocontato_detail.html"
    context_object_name = "secaocontato"

    def get_context_data(self, **kwargs):
        context = super(SecaoContatoDetailView, self).get_context_data(**kwargs)
        return context


class SecaoContatoCreateView(BaseCreateView):
    """Classe para gerenciar o create do SecaoContato"""

    model = SecaoContato
    form_class = SecaoContatoForm
    context_object_name = "secaocontato"
    success_url = "portifolio:secaocontato-list"
    template_name = "portifolio/secaocontato/secaocontato_create.html"
    # inlines = []
    # form_modals = []


class SecaoContatoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do SecaoContato"""

    model = SecaoContato
    form_class = SecaoContatoForm
    context_object_name = "secaocontato"
    success_url = "portifolio:secaocontato-list"
    template_name = "portifolio/secaocontato/secaocontato_update.html"
    # inlines = []
    # form_modals = []


class SecaoContatoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do SecaoContato"""

    model = SecaoContato
    form_class = SecaoContatoForm
    context_object_name = "secaocontato"
    success_url = "portifolio:secaocontato-list"
    template_name = "portifolio/secaocontato/secaocontato_delete.html"


class SecaoContatoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do SecaoContato"""

    model = SecaoContato
    context_object_name = "secaocontato"
    success_url = "portifolio:secaocontato-list"
    template_name = "portifolio/secaocontato/secaocontato_restore.html"


# Fim das Views do Models SecaoContato
