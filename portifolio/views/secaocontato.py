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
from usuario.models import Usuario


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
        qs = super(SecaoContatoListView, self).get_queryset()
        # Se o usuário for um superusuário, retorna todos os registros.
        if self.request.user.is_superuser:
            return qs
        # Caso contrário, filtra os registros associados ao usuário logado.
        usuario_instance = self.request.user.usuario
        return qs.filter(usuario=usuario_instance)


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
    def form_valid(self, form):
        # Converter request.user para uma instância de Usuario;
        # supondo que haja uma relação OneToOne entre os dois modelos:
        usuario_instance = self.request.user.usuario
        # Caso não haja OneToOne, utilize outro critério, por exemplo:
        usuario_instance = Usuario.objects.get(email=self.request.user.email)

        form.instance.usuario = usuario_instance
        return super().form_valid(form)

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
