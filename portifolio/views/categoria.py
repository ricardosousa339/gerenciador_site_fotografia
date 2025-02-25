from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.categoria import CategoriaForm
from portifolio.models import Categoria
from usuario.models import Usuario


# Views do Models Categoria
class CategoriaListView(BaseListView):
    """Classe para gerenciar a listagem do Categoria"""

    model = Categoria
    template_name = "portifolio/categoria/categoria_list.html"
    context_object_name = "categoria"
    list_display = ["nome"]
    search_fields = ["nome"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """
        qs = super(CategoriaListView, self).get_queryset()
        # Se o usuário for um superusuário, retorna todos os registros.
        if self.request.user.is_superuser:
            return qs
        # Caso contrário, filtra os registros associados ao usuário logado.
        usuario_instance = self.request.user.usuario
        return qs.filter(usuario=usuario_instance)


class CategoriaDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Categoria"""

    model = Categoria
    form_class = CategoriaForm
    success_url = "portifolio:categoria-list"
    template_name = "portifolio/categoria/categoria_detail.html"
    context_object_name = "categoria"

    def get_context_data(self, **kwargs):
        context = super(CategoriaDetailView, self).get_context_data(**kwargs)
        return context


class CategoriaCreateView(BaseCreateView):
    """Classe para gerenciar o create do Categoria"""

    model = Categoria
    form_class = CategoriaForm
    context_object_name = "categoria"
    success_url = "portifolio:categoria-list"
    template_name = "portifolio/categoria/categoria_create.html"

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


class CategoriaUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Categoria"""

    model = Categoria
    form_class = CategoriaForm
    context_object_name = "categoria"
    success_url = "portifolio:categoria-list"
    template_name = "portifolio/categoria/categoria_update.html"
    # inlines = []
    # form_modals = []


class CategoriaDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Categoria"""

    model = Categoria
    form_class = CategoriaForm
    context_object_name = "categoria"
    success_url = "portifolio:categoria-list"
    template_name = "portifolio/categoria/categoria_delete.html"


class CategoriaRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Categoria"""

    model = Categoria
    context_object_name = "categoria"
    success_url = "portifolio:categoria-list"
    template_name = "portifolio/categoria/categoria_restore.html"


# Fim das Views do Models Categoria
