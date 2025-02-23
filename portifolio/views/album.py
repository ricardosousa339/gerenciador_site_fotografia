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
