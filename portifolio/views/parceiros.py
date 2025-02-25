from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.parceiros import ParceirosForm
from portifolio.models import Parceiros
from usuario.models import Usuario


# Views do Models Parceiros
class ParceirosListView(BaseListView):
    """Classe para gerenciar a listagem do Parceiros"""

    model = Parceiros
    template_name = "portifolio/parceiros/parceiros_list.html"
    context_object_name = "parceiros"

    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ParceirosListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(ParceirosListView, self).get_queryset()
        return queryset


class ParceirosDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Parceiros"""

    model = Parceiros
    form_class = ParceirosForm
    success_url = "portifolio:parceiros-list"
    template_name = "portifolio/parceiros/parceiros_detail.html"
    context_object_name = "parceiros"

    def get_context_data(self, **kwargs):
        context = super(ParceirosDetailView, self).get_context_data(**kwargs)
        return context


class ParceirosCreateView(BaseCreateView):
    """Classe para gerenciar o create do Parceiros"""

    model = Parceiros
    form_class = ParceirosForm
    context_object_name = "parceiros"
    success_url = "portifolio:parceiros-list"
    template_name = "portifolio/parceiros/parceiros_create.html"
    # inlines = []
    # form_modals = []
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as fotos para incluir apenas as do usuário logado
        form.fields["logo"].queryset = form.fields["logo"].queryset.filter(
            usuario=self.request.user.usuario, deleted=False, enabled=True
        )
        return form
    def form_valid(self, form):

        usuario_instance = self.request.user.usuario
        usuario_instance = Usuario.objects.get(email=self.request.user.email)

        form.instance.usuario = usuario_instance
        return super().form_valid(form)

class ParceirosUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Parceiros"""

    model = Parceiros
    form_class = ParceirosForm
    context_object_name = "parceiros"
    success_url = "portifolio:parceiros-list"
    template_name = "portifolio/parceiros/parceiros_update.html"
    # inlines = []
    # form_modals = []


class ParceirosDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Parceiros"""

    model = Parceiros
    form_class = ParceirosForm
    context_object_name = "parceiros"
    success_url = "portifolio:parceiros-list"
    template_name = "portifolio/parceiros/parceiros_delete.html"


class ParceirosRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Parceiros"""

    model = Parceiros
    context_object_name = "parceiros"
    success_url = "portifolio:parceiros-list"
    template_name = "portifolio/parceiros/parceiros_restore.html"


# Fim das Views do Models Parceiros
