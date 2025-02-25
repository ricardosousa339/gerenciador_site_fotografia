from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.album import AlbumForm
from portifolio.models import Album
from usuario.models import Usuario


# Views do Models Album
class AlbumListView(BaseListView):
    """Classe para gerenciar a listagem do Album"""

    model = Album
    template_name = "portifolio/album/album_list.html"
    context_object_name = "album"
    list_display = ["titulo", "url", "usuario"]
    search_fields = ["titulo", "url", "usuario"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(AlbumListView, self).get_queryset()
        return queryset


class AlbumDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do Album"""

    model = Album
    form_class = AlbumForm
    success_url = "portifolio:album-list"
    template_name = "portifolio/album/album_detail.html"
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['fotos'] = self.object.fotos.all()  # Ajuste se o related_name for diferente
        return context


class AlbumCreateView(BaseCreateView):
    """Classe para gerenciar o create do Album"""

    model = Album
    form_class = AlbumForm
    context_object_name = "album"
    success_url = "portifolio:album-list"
    template_name = "portifolio/album/album_create.html"
    # inlines = []
    # form_modals = []
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as fotos para incluir apenas as do usuário logado
        form.fields['fotos'].queryset = form.fields['fotos'].queryset.filter(
            usuario=self.request.user.usuario,
            deleted=False,
            enabled=True
        )
        return form
    
    def form_valid(self, form):
        # Converter request.user para uma instância de Usuario; 
        # supondo que haja uma relação OneToOne entre os dois modelos:
        usuario_instance = self.request.user.usuario  
        # Caso não haja OneToOne, utilize outro critério, por exemplo:
        usuario_instance = Usuario.objects.get(email=self.request.user.email)
        
        form.instance.usuario = usuario_instance
        return super().form_valid(form)


class AlbumUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do Album"""

    model = Album
    form_class = AlbumForm
    context_object_name = "album"
    success_url = "portifolio:album-list"
    template_name = "portifolio/album/album_update.html"
    # inlines = []
    # form_modals = []


class AlbumDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do Album"""

    model = Album
    form_class = AlbumForm
    context_object_name = "album"
    success_url = "portifolio:album-list"
    template_name = "portifolio/album/album_delete.html"


class AlbumRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do Album"""

    model = Album
    context_object_name = "album"
    success_url = "portifolio:album-list"
    template_name = "portifolio/album/album_restore.html"


# Fim das Views do Models Album
