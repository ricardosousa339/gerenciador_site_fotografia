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
from usuario.models import Usuario


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
        qs = super(FotoListView, self).get_queryset()
        # Se o usuário for um superusuário, retorna todos os registros.
        if self.request.user.is_superuser:
            return qs
        # Caso contrário, filtra os registros associados ao usuário logado.
        usuario_instance = self.request.user.usuario
        return qs.filter(usuario=usuario_instance)

        # queryset = super(FotoListView, self).get_queryset()
        # return queryset


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

    def form_valid(self, form):
        # Converter request.user para uma instância de Usuario;
        # supondo que haja uma relação OneToOne entre os dois modelos:
        usuario_instance = self.request.user.usuario
        # Caso não haja OneToOne, utilize outro critério, por exemplo:
        usuario_instance = Usuario.objects.get(email=self.request.user.email)

        form.instance.usuario = usuario_instance
        return super().form_valid(form)


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
