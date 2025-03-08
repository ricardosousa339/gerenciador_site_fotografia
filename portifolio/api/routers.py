from rest_framework import routers

from portifolio.api.views.album import AlbumReadOnlyAPI, AlbumViewAPI
from portifolio.api.views.categoria import CategoriaReadOnlyAPI, CategoriaViewAPI
from portifolio.api.views.dadosprincipais import (
    DadosPrincipaisReadOnlyAPI,
    DadosPrincipaisViewAPI,
)
from portifolio.api.views.fatosobre import FatoSobreReadOnlyAPI, FatoSobreViewAPI
from portifolio.api.views.foto import FotoReadOnlyAPI, FotoViewAPI
from portifolio.api.views.imagemheader import (
    ImagemHeaderReadOnlyAPI,
    ImagemHeaderViewAPI,
)
from portifolio.api.views.mensagemcontato import (
    MensagemContatoReadOnlyAPI,
    MensagemContatoViewAPI,
)
from portifolio.api.views.parceiros import ParceirosReadOnlyAPI, ParceirosViewAPI
from portifolio.api.views.secaocontato import (
    SecaoContatoReadOnlyAPI,
    SecaoContatoViewAPI,
)
from portifolio.api.views.secaosobre import SecaoSobreReadOnlyAPI, SecaoSobreViewAPI

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


# URL para a API Categoria
router.register(r"categoria", CategoriaViewAPI, "categoria-api")
router.register(r"categoria_readonly", CategoriaReadOnlyAPI, "categoria-readonly-api")


# URL para a API SecaoSobre
router.register(r"secaosobre", SecaoSobreViewAPI, "secaosobre-api")
router.register(
    r"secaosobre_readonly", SecaoSobreReadOnlyAPI, "secaosobre-readonly-api"
)


# URL para a API FatoSobre
router.register(r"fatosobre", FatoSobreViewAPI, "fatosobre-api")
router.register(r"fatosobre_readonly", FatoSobreReadOnlyAPI, "fatosobre-readonly-api")


# URL para a API MensagemContato
router.register(r"mensagemcontato", MensagemContatoViewAPI, "mensagemcontato-api")
router.register(
    r"mensagemcontato_readonly",
    MensagemContatoReadOnlyAPI,
    "mensagemcontato-readonly-api",
)


# URL para a API Parceiros
router.register(r"parceiros", ParceirosViewAPI, "parceiros-api")
router.register(r"parceiros_readonly", ParceirosReadOnlyAPI, "parceiros-readonly-api")


# URL para a API DadosPrincipais
router.register(r"dadosprincipais", DadosPrincipaisViewAPI, "dadosprincipais-api")
router.register(
    r"dadosprincipais_readonly",
    DadosPrincipaisReadOnlyAPI,
    "dadosprincipais-readonly-api",
)


# URL para a API SecaoContato
router.register(r"secaocontato", SecaoContatoViewAPI, "secaocontato-api")
router.register(
    r"secaocontato_readonly", SecaoContatoReadOnlyAPI, "secaocontato-readonly-api"
)


urlpatterns = router.urls
