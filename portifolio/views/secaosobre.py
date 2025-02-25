from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.secaosobre import SecaoSobreForm
from portifolio.models import SecaoSobre


# Views do Models SecaoSobre
class SecaoSobreListView(BaseListView):
    """Classe para gerenciar a listagem do SecaoSobre"""

    model = SecaoSobre
    template_name = "portifolio/secaosobre/secaosobre_list.html"
    context_object_name = "secaosobre"

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SecaoSobreListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(SecaoSobreListView, self).get_queryset()
        return queryset


class SecaoSobreDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do SecaoSobre"""

    model = SecaoSobre
    form_class = SecaoSobreForm
    success_url = "portifolio:secaosobre-list"
    template_name = "portifolio/secaosobre/secaosobre_detail.html"
    context_object_name = "secaosobre"

    def get_context_data(self, **kwargs):
        context = super(SecaoSobreDetailView, self).get_context_data(**kwargs)
        return context


class SecaoSobreCreateView(BaseCreateView):
    """Classe para gerenciar o create do SecaoSobre"""

    model = SecaoSobre
    form_class = SecaoSobreForm
    context_object_name = "secaosobre"
    success_url = "portifolio:secaosobre-list"
    template_name = "portifolio/secaosobre/secaosobre_create.html"
    # inlines = []
    # form_modals = []


class SecaoSobreUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do SecaoSobre"""

    model = SecaoSobre
    form_class = SecaoSobreForm
    context_object_name = "secaosobre"
    success_url = "portifolio:secaosobre-list"
    template_name = "portifolio/secaosobre/secaosobre_update.html"
    # inlines = []
    # form_modals = []


class SecaoSobreDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do SecaoSobre"""

    model = SecaoSobre
    form_class = SecaoSobreForm
    context_object_name = "secaosobre"
    success_url = "portifolio:secaosobre-list"
    template_name = "portifolio/secaosobre/secaosobre_delete.html"


class SecaoSobreRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do SecaoSobre"""

    model = SecaoSobre
    context_object_name = "secaosobre"
    success_url = "portifolio:secaosobre-list"
    template_name = "portifolio/secaosobre/secaosobre_restore.html"


# Fim das Views do Models SecaoSobre
