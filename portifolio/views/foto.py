from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.foto import FotoForm
from portifolio.models import Foto


# Views do Models Foto
class FotoListView(BaseListView):
    """Classe para gerenciar a listagem do Foto"""

    model = Foto
    template_name = "portifolio/foto/foto_list.html"
    context_object_name = "foto"
    list_display = ["nome"]
    search_fields = ["nome"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FotoListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(FotoListView, self).get_queryset()
        return queryset


class FotoDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Foto"""

    model = Foto
    form_class = FotoForm
    success_url = "portifolio:foto-list"
    template_name = "portifolio/foto/foto_detail.html"
    context_object_name = "foto"

    def get_context_data(self, **kwargs):
        context = super(FotoDetailView, self).get_context_data(**kwargs)
        return context


class FotoCreateView(BaseCreateView):
    """Classe para gerenciar o create do Foto"""

    model = Foto
    form_class = FotoForm
    context_object_name = "foto"
    success_url = "portifolio:foto-list"
    template_name = "portifolio/foto/foto_create.html"
    # inlines = []
    # form_modals = []


class FotoUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Foto"""

    model = Foto
    form_class = FotoForm
    context_object_name = "foto"
    success_url = "portifolio:foto-list"
    template_name = "portifolio/foto/foto_update.html"
    # inlines = []
    # form_modals = []


class FotoDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Foto"""

    model = Foto
    form_class = FotoForm
    context_object_name = "foto"
    success_url = "portifolio:foto-list"
    template_name = "portifolio/foto/foto_delete.html"


class FotoRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Foto"""

    model = Foto
    context_object_name = "foto"
    success_url = "portifolio:foto-list"
    template_name = "portifolio/foto/foto_restore.html"


# Fim das Views do Models Foto
