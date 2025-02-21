from rest_framework import routers

from usuario.api.views.usuario import UsuarioReadOnlyAPI, UsuarioViewAPI

router = routers.DefaultRouter()

# URL para a API Usuario
router.register(r"usuario", UsuarioViewAPI, "usuario-api")
router.register(r"usuario_readonly", UsuarioReadOnlyAPI, "usuario-readonly-api")

urlpatterns = router.urls
