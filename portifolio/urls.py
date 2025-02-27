from django.urls import path

from portifolio.views.album import (
    AlbumCreateView,
    AlbumDeleteView,
    AlbumDetailView,
    AlbumListView,
    AlbumRestoreView,
    AlbumUpdateView,
)
from portifolio.views.categoria import (
    CategoriaCreateView,
    CategoriaDeleteView,
    CategoriaDetailView,
    CategoriaListView,
    CategoriaRestoreView,
    CategoriaUpdateView,
)
from portifolio.views.fatosobre import (
    FatoSobreCreateView,
    FatoSobreDeleteView,
    FatoSobreDetailView,
    FatoSobreListView,
    FatoSobreRestoreView,
    FatoSobreUpdateView,
)
from portifolio.views.foto import (
    FotoCreateView,
    FotoDeleteView,
    FotoDetailView,
    FotoListView,
    FotoRestoreView,
    FotoUpdateView,
)
from portifolio.views.imagemheader import (
    ImagemHeaderCreateView,
    ImagemHeaderDeleteView,
    ImagemHeaderDetailView,
    ImagemHeaderListView,
    ImagemHeaderRestoreView,
    ImagemHeaderUpdateView,
)
from portifolio.views.index import PortifolioIndexTemplateView
from portifolio.views.mensagemcontato import (
    MensagemContatoCreateView,
    MensagemContatoDeleteView,
    MensagemContatoDetailView,
    MensagemContatoListView,
    MensagemContatoRestoreView,
    MensagemContatoUpdateView,
)
from portifolio.views.parceiros import (
    ParceirosCreateView,
    ParceirosDeleteView,
    ParceirosDetailView,
    ParceirosListView,
    ParceirosRestoreView,
    ParceirosUpdateView,
)
from portifolio.views.secaosobre import (
    SecaoSobreCreateView,
    SecaoSobreDeleteView,
    SecaoSobreDetailView,
    SecaoSobreListView,
    SecaoSobreRestoreView,
    SecaoSobreUpdateView,
)
from portifolio.views.webhook import webhook_deploy

app_name = "portifolio"
urlpatterns = [
    path("portifolio/", PortifolioIndexTemplateView.as_view(), name="portifolio-index"),
]

# URLs do Models Album
urlpatterns += [
    path("portifolio/album/", AlbumListView.as_view(), name="album-list"),
    path("portifolio/album/create/", AlbumCreateView.as_view(), name="album-create"),
    path("portifolio/album/<uuid:pk>/", AlbumDetailView.as_view(), name="album-detail"),
    path(
        "portifolio/album/update/<uuid:pk>/",
        AlbumUpdateView.as_view(),
        name="album-update",
    ),
    path(
        "portifolio/album/delete/<uuid:pk>/",
        AlbumDeleteView.as_view(),
        name="album-delete",
    ),
    path(
        "portifolio/album/restore/<uuid:pk>/",
        AlbumRestoreView.as_view(),
        name="album-restore",
    ),
]

# URLs do Models Foto
urlpatterns += [
    path("portifolio/foto/", FotoListView.as_view(), name="foto-list"),
    path("portifolio/foto/create/", FotoCreateView.as_view(), name="foto-create"),
    path("portifolio/foto/<uuid:pk>/", FotoDetailView.as_view(), name="foto-detail"),
    path(
        "portifolio/foto/update/<uuid:pk>/",
        FotoUpdateView.as_view(),
        name="foto-update",
    ),
    path(
        "portifolio/foto/delete/<uuid:pk>/",
        FotoDeleteView.as_view(),
        name="foto-delete",
    ),
    path(
        "portifolio/foto/restore/<uuid:pk>/",
        FotoRestoreView.as_view(),
        name="foto-restore",
    ),
]

# URLs do Models ImagemHeader
urlpatterns += [
    path(
        "portifolio/imagemheader/",
        ImagemHeaderListView.as_view(),
        name="imagemheader-list",
    ),
    path(
        "portifolio/imagemheader/create/",
        ImagemHeaderCreateView.as_view(),
        name="imagemheader-create",
    ),
    path(
        "portifolio/imagemheader/<uuid:pk>/",
        ImagemHeaderDetailView.as_view(),
        name="imagemheader-detail",
    ),
    path(
        "portifolio/imagemheader/update/<uuid:pk>/",
        ImagemHeaderUpdateView.as_view(),
        name="imagemheader-update",
    ),
    path(
        "portifolio/imagemheader/delete/<uuid:pk>/",
        ImagemHeaderDeleteView.as_view(),
        name="imagemheader-delete",
    ),
    path(
        "portifolio/imagemheader/restore/<uuid:pk>/",
        ImagemHeaderRestoreView.as_view(),
        name="imagemheader-restore",
    ),
]

# URLs do Models Categoria
urlpatterns += [
    path("portifolio/categoria/", CategoriaListView.as_view(), name="categoria-list"),
    path(
        "portifolio/categoria/create/",
        CategoriaCreateView.as_view(),
        name="categoria-create",
    ),
    path(
        "portifolio/categoria/<uuid:pk>/",
        CategoriaDetailView.as_view(),
        name="categoria-detail",
    ),
    path(
        "portifolio/categoria/update/<uuid:pk>/",
        CategoriaUpdateView.as_view(),
        name="categoria-update",
    ),
    path(
        "portifolio/categoria/delete/<uuid:pk>/",
        CategoriaDeleteView.as_view(),
        name="categoria-delete",
    ),
    path(
        "portifolio/categoria/restore/<uuid:pk>/",
        CategoriaRestoreView.as_view(),
        name="categoria-restore",
    ),
]

# URLs do Models SecaoSobre
urlpatterns += [
    path(
        "portifolio/secaosobre/", SecaoSobreListView.as_view(), name="secaosobre-list"
    ),
    path(
        "portifolio/secaosobre/create/",
        SecaoSobreCreateView.as_view(),
        name="secaosobre-create",
    ),
    path(
        "portifolio/secaosobre/<uuid:pk>/",
        SecaoSobreDetailView.as_view(),
        name="secaosobre-detail",
    ),
    path(
        "portifolio/secaosobre/update/<uuid:pk>/",
        SecaoSobreUpdateView.as_view(),
        name="secaosobre-update",
    ),
    path(
        "portifolio/secaosobre/delete/<uuid:pk>/",
        SecaoSobreDeleteView.as_view(),
        name="secaosobre-delete",
    ),
    path(
        "portifolio/secaosobre/restore/<uuid:pk>/",
        SecaoSobreRestoreView.as_view(),
        name="secaosobre-restore",
    ),
]

# URLs do Models FatoSobre
urlpatterns += [
    path("portifolio/fatosobre/", FatoSobreListView.as_view(), name="fatosobre-list"),
    path(
        "portifolio/fatosobre/create/",
        FatoSobreCreateView.as_view(),
        name="fatosobre-create",
    ),
    path(
        "portifolio/fatosobre/<uuid:pk>/",
        FatoSobreDetailView.as_view(),
        name="fatosobre-detail",
    ),
    path(
        "portifolio/fatosobre/update/<uuid:pk>/",
        FatoSobreUpdateView.as_view(),
        name="fatosobre-update",
    ),
    path(
        "portifolio/fatosobre/delete/<uuid:pk>/",
        FatoSobreDeleteView.as_view(),
        name="fatosobre-delete",
    ),
    path(
        "portifolio/fatosobre/restore/<uuid:pk>/",
        FatoSobreRestoreView.as_view(),
        name="fatosobre-restore",
    ),
]

# URLs do Models MensagemContato
urlpatterns += [
    path(
        "portifolio/mensagemcontato/",
        MensagemContatoListView.as_view(),
        name="mensagemcontato-list",
    ),
    path(
        "portifolio/mensagemcontato/create/",
        MensagemContatoCreateView.as_view(),
        name="mensagemcontato-create",
    ),
    path(
        "portifolio/mensagemcontato/<uuid:pk>/",
        MensagemContatoDetailView.as_view(),
        name="mensagemcontato-detail",
    ),
    path(
        "portifolio/mensagemcontato/update/<uuid:pk>/",
        MensagemContatoUpdateView.as_view(),
        name="mensagemcontato-update",
    ),
    path(
        "portifolio/mensagemcontato/delete/<uuid:pk>/",
        MensagemContatoDeleteView.as_view(),
        name="mensagemcontato-delete",
    ),
    path(
        "portifolio/mensagemcontato/restore/<uuid:pk>/",
        MensagemContatoRestoreView.as_view(),
        name="mensagemcontato-restore",
    ),
]

# URLs do Models Parceiros
urlpatterns += [
    path("portifolio/parceiros/", ParceirosListView.as_view(), name="parceiros-list"),
    path(
        "portifolio/parceiros/create/",
        ParceirosCreateView.as_view(),
        name="parceiros-create",
    ),
    path(
        "portifolio/parceiros/<uuid:pk>/",
        ParceirosDetailView.as_view(),
        name="parceiros-detail",
    ),
    path(
        "portifolio/parceiros/update/<uuid:pk>/",
        ParceirosUpdateView.as_view(),
        name="parceiros-update",
    ),
    path(
        "portifolio/parceiros/delete/<uuid:pk>/",
        ParceirosDeleteView.as_view(),
        name="parceiros-delete",
    ),
    path(
        "portifolio/parceiros/restore/<uuid:pk>/",
        ParceirosRestoreView.as_view(),
        name="parceiros-restore",
    ),
]

urlpatterns = [
    path('portifolio/webhook/deploy/', webhook_deploy, name='deploy-webhook'),
]

