from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.dadosprincipais import DadosPrincipaisForm
from portifolio.models import DadosPrincipais


# Views do Models DadosPrincipais
class DadosPrincipaisListView(BaseListView):
    """Classe para gerenciar a listagem do DadosPrincipais"""

    model = DadosPrincipais
    template_name = "portifolio/dadosprincipais/dadosprincipais_list.html"
    context_object_name = "dadosprincipais"
    list_display = ["nome", "subtitulo"]
    search_fields = ["nome", "subtitulo"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DadosPrincipaisListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(DadosPrincipaisListView, self).get_queryset()
        return queryset


class DadosPrincipaisDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do DadosPrincipais"""

    model = DadosPrincipais
    form_class = DadosPrincipaisForm
    success_url = "portifolio:dadosprincipais-list"
    template_name = "portifolio/dadosprincipais/dadosprincipais_detail.html"
    context_object_name = "dadosprincipais"

    def get_context_data(self, **kwargs):
        context = super(DadosPrincipaisDetailView, self).get_context_data(**kwargs)
        return context


class DadosPrincipaisCreateView(BaseCreateView):
    """Classe para gerenciar o create do DadosPrincipais"""

    model = DadosPrincipais
    form_class = DadosPrincipaisForm
    context_object_name = "dadosprincipais"
    success_url = "portifolio:dadosprincipais-list"
    template_name = "portifolio/dadosprincipais/dadosprincipais_create.html"
    # inlines = []
    # form_modals = []


class DadosPrincipaisUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do DadosPrincipais"""

    model = DadosPrincipais
    form_class = DadosPrincipaisForm
    context_object_name = "dadosprincipais"
    success_url = "portifolio:dadosprincipais-list"
    template_name = "portifolio/dadosprincipais/dadosprincipais_update.html"
    # inlines = []
    # form_modals = []


class DadosPrincipaisDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do DadosPrincipais"""

    model = DadosPrincipais
    form_class = DadosPrincipaisForm
    context_object_name = "dadosprincipais"
    success_url = "portifolio:dadosprincipais-list"
    template_name = "portifolio/dadosprincipais/dadosprincipais_delete.html"


class DadosPrincipaisRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do DadosPrincipais"""

    model = DadosPrincipais
    context_object_name = "dadosprincipais"
    success_url = "portifolio:dadosprincipais-list"
    template_name = "portifolio/dadosprincipais/dadosprincipais_restore.html"


# Fim das Views do Models DadosPrincipais
