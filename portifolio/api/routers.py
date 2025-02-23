from rest_framework import routers

from portifolio.api.views.album import AlbumReadOnlyAPI, AlbumViewAPI
from portifolio.api.views.foto import FotoReadOnlyAPI, FotoViewAPI
from portifolio.api.views.imagemheader import (
    ImagemHeaderReadOnlyAPI,
    ImagemHeaderViewAPI,
)

router = routers.DefaultRouter()

# URL para a API Album
router.register(r"album", AlbumViewAPI, "album-api")
router.register(r"album_readonly", AlbumReadOnlyAPI, "album-readonly-api")


# URL para a API Foto
router.register(r"foto", FotoViewAPI, "foto-api")
router.register(r"foto_readonly", FotoReadOnlyAPI, "foto-readonly-api")


# URL para a API ImagemHeader
router.register(r"imagemheader", ImagemHeaderViewAPI, "imagemheader-api")
router.register(
    r"imagemheader_readonly", ImagemHeaderReadOnlyAPI, "imagemheader-readonly-api"
)


urlpatterns = router.urls
