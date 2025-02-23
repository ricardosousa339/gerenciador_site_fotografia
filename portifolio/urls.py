from django.urls import path

from portifolio.views.album import (
    AlbumCreateView,
    AlbumDeleteView,
    AlbumDetailView,
    AlbumListView,
    AlbumRestoreView,
    AlbumUpdateView,
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
