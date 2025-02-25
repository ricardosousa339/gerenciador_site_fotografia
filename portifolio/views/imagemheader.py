from core.views.base import (
    BaseCreateView,
    BaseDeleteView,
    BaseDetailView,
    BaseListView,
    BaseRestoreView,
    BaseUpdateView,
)
from portifolio.forms.imagemheader import ImagemHeaderForm
from portifolio.models import ImagemHeader
from usuario.models import Usuario


# Views do Models ImagemHeader
class ImagemHeaderListView(BaseListView):
    """Classe para gerenciar a listagem do ImagemHeader"""

    model = ImagemHeader
    template_name = "portifolio/imagemheader/imagemheader_list.html"
    context_object_name = "imagemheader"
    list_display = ["imagem"]
    search_fields = ["imagem"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ImagemHeaderListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """Subscrevendo o queryset para
        filtrar os dados conforme o perfil logado

        Returns:
            QuerySet
        """

        queryset = super(ImagemHeaderListView, self).get_queryset()
        return queryset


class ImagemHeaderDetailView(BaseDetailView):
    """Classe para gerenciar o detalhe do ImagemHeader"""

    model = ImagemHeader
    form_class = ImagemHeaderForm
    success_url = "portifolio:imagemheader-list"
    template_name = "portifolio/imagemheader/imagemheader_detail.html"
    context_object_name = "imagemheader"

    def get_context_data(self, **kwargs):
        context = super(ImagemHeaderDetailView, self).get_context_data(**kwargs)
        return context


class ImagemHeaderCreateView(BaseCreateView):
    """Classe para gerenciar o create do ImagemHeader"""

    model = ImagemHeader
    form_class = ImagemHeaderForm
    context_object_name = "imagemheader"
    success_url = "portifolio:imagemheader-list"
    template_name = "portifolio/imagemheader/imagemheader_create.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as fotos para incluir apenas as do usuário logado
        form.fields['imagem'].queryset = form.fields['imagem'].queryset.filter(
            usuario=self.request.user.usuario,
            deleted=False,
            enabled=True
        )
        return form

    def form_valid(self, form):
        usuario_instance = self.request.user.usuario  
        usuario_instance = Usuario.objects.get(email=self.request.user.email)
        form.instance.usuario = usuario_instance
        return super().form_valid(form)


class ImagemHeaderUpdateView(BaseUpdateView):
    """Classe para gerenciar a update do ImagemHeader"""

    model = ImagemHeader
    form_class = ImagemHeaderForm
    context_object_name = "imagemheader"
    success_url = "portifolio:imagemheader-list"
    template_name = "portifolio/imagemheader/imagemheader_update.html"
    # inlines = []
    # form_modals = []


class ImagemHeaderDeleteView(BaseDeleteView):
    """Classe para gerenciar o delete do ImagemHeader"""

    model = ImagemHeader
    form_class = ImagemHeaderForm
    context_object_name = "imagemheader"
    success_url = "portifolio:imagemheader-list"
    template_name = "portifolio/imagemheader/imagemheader_delete.html"


class ImagemHeaderRestoreView(BaseRestoreView):
    """Classe para gerenciar o restore do ImagemHeader"""

    model = ImagemHeader
    context_object_name = "imagemheader"
    success_url = "portifolio:imagemheader-list"
    template_name = "portifolio/imagemheader/imagemheader_restore.html"


# Fim das Views do Models ImagemHeader
