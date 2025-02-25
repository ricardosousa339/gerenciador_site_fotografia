from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.fatosobre import FatoSobreForm
from portifolio.models import FatoSobre


# Views do Models FatoSobre
class FatoSobreListView(BaseListView):
    """Classe para gerenciar a listagem do FatoSobre"""

    model = FatoSobre
    template_name = "portifolio/fatosobre/fatosobre_list.html"
    context_object_name = "fatosobre"
    list_display = ["titulo"]
    search_fields = ["titulo"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FatoSobreListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(FatoSobreListView, self).get_queryset()
        return queryset


class FatoSobreDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do FatoSobre"""

    model = FatoSobre
    form_class = FatoSobreForm
    success_url = "portifolio:fatosobre-list"
    template_name = "portifolio/fatosobre/fatosobre_detail.html"
    context_object_name = "fatosobre"

    def get_context_data(self, **kwargs):
        context = super(FatoSobreDetailView, self).get_context_data(**kwargs)
        return context


class FatoSobreCreateView(BaseCreateView):
    """Classe para gerenciar o create do FatoSobre"""

    model = FatoSobre
    form_class = FatoSobreForm
    context_object_name = "fatosobre"
    success_url = "portifolio:fatosobre-list"
    template_name = "portifolio/fatosobre/fatosobre_create.html"
    # inlines = []
    # form_modals = []


class FatoSobreUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do FatoSobre"""

    model = FatoSobre
    form_class = FatoSobreForm
    context_object_name = "fatosobre"
    success_url = "portifolio:fatosobre-list"
    template_name = "portifolio/fatosobre/fatosobre_update.html"
    # inlines = []
    # form_modals = []


class FatoSobreDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do FatoSobre"""

    model = FatoSobre
    form_class = FatoSobreForm
    context_object_name = "fatosobre"
    success_url = "portifolio:fatosobre-list"
    template_name = "portifolio/fatosobre/fatosobre_delete.html"


class FatoSobreRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do FatoSobre"""

    model = FatoSobre
    context_object_name = "fatosobre"
    success_url = "portifolio:fatosobre-list"
    template_name = "portifolio/fatosobre/fatosobre_restore.html"


# Fim das Views do Models FatoSobre
