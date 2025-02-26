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
from usuario.models import Usuario


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
        qs = super(FatoSobreListView, self).get_queryset()
        # Se o usuário for um superusuário, retorna todos os registros.
        if self.request.user.is_superuser:
            return qs
        # Caso contrário, filtra os registros associados ao usuário logado.
        usuario_instance = self.request.user.usuario
        return qs.filter(usuario=usuario_instance)


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

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     # Filtra as fotos para incluir apenas as do usuário logado
    #     form.fields["secao_sobre"].queryset = form.fields["secao_sobre"].queryset.filter(
    #         usuario=self.request.user.usuario, deleted=False, enabled=True
    #     )
    #     return form
    
    def form_valid(self, form):

        usuario_instance = self.request.user.usuario
        usuario_instance = Usuario.objects.get(email=self.request.user.email)

        form.instance.usuario = usuario_instance
        return super().form_valid(form)

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
