from rest_framework import routers

from configuracao_core.api.views.dadosgerais import (
    DadosGeraisReadOnlyAPI,
    DadosGeraisViewAPI,
)
from configuracao_core.api.views.gestor import GestorReadOnlyAPI, GestorViewAPI
from configuracao_core.api.views.imagemgenerica import (
    ImagemGenericaReadOnlyAPI,
    ImagemGenericaViewAPI,
)
from configuracao_core.api.views.imagemlogin import (
    ImagemLoginReadOnlyAPI,
    ImagemLoginViewAPI,
)
from configuracao_core.api.views.imagenssistema import (
    ImagensSistemaReadOnlyAPI,
    ImagensSistemaViewAPI,
)
from configuracao_core.api.views.logosistema import (
    LogoSistemaReadOnlyAPI,
    LogoSistemaViewAPI,
)
from configuracao_core.api.views.redesocial import (
    RedeSocialReadOnlyAPI,
    RedeSocialViewAPI,
)

router = routers.DefaultRouter()

# URL para a API Gestor
router.register(r"gestor", GestorViewAPI, "gestor-api")
router.register(r"gestor_readonly", GestorReadOnlyAPI, "gestor-readonly-api")


# URL para a API ImagemLogin
router.register(r"imagemlogin", ImagemLoginViewAPI, "imagemlogin-api")
router.register(
    r"imagemlogin_readonly", ImagemLoginReadOnlyAPI, "imagemlogin-readonly-api"
)


# URL para a API LogoSistema
router.register(r"logosistema", LogoSistemaViewAPI, "logosistema-api")
router.register(
    r"logosistema_readonly", LogoSistemaReadOnlyAPI, "logosistema-readonly-api"
)


# URL para a API DadosGerais
router.register(r"dadosgerais", DadosGeraisViewAPI, "dadosgerais-api")
router.register(
    r"dadosgerais_readonly", DadosGeraisReadOnlyAPI, "dadosgerais-readonly-api"
)


# URL para a API RedeSocial
router.register(r"redesocial", RedeSocialViewAPI, "redesocial-api")
router.register(
    r"redesocial_readonly", RedeSocialReadOnlyAPI, "redesocial-readonly-api"
)


# URL para a API ImagemGenerica
router.register(r"imagemgenerica", ImagemGenericaViewAPI, "imagemgenerica-api")
router.register(
    r"imagemgenerica_readonly", ImagemGenericaReadOnlyAPI, "imagemgenerica-readonly-api"
)


# URL para a API ImagensSistema
router.register(r"imagenssistema", ImagensSistemaViewAPI, "imagenssistema-api")
router.register(
    r"imagenssistema_readonly", ImagensSistemaReadOnlyAPI, "imagenssistema-readonly-api"
)


urlpatterns = router.urls
