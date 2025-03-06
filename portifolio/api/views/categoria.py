from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from portifolio.api.serializers.categoria import CategoriaSerializer
from portifolio.models import Categoria


class CategoriaViewAPI(ModelViewSet):
    """Classe para gerenciar as requisições da API para POST, PUT, PATCH e DELETE

    A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    buscas no models como por exemplo search=valor_a_ser_pesquisado

    Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """

    # TODO: Enviar apenas as categorias do usuário logado (as outras coisas também)
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.select_related().filter(deleted=False)
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = []
    ordering_fields = []

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(usuario=self.request.user.usuario, deleted=False)

class CategoriaReadOnlyAPI(OptimizedQuerySetMixin, ReadOnlyModelViewSet):
    """Classe para gerenciar as requisições da API GET com apenas leitura

    A lista search_fields deve ser configurada com os campos do models que poderão ser utilizados para realizar
    buscas no models como por exemplo search=valor_a_ser_pesquisado

    Retorne apenas os campos desejados com o parâmetro fields=campo1,campo2
    """

    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.select_related().all()
    serializer_class = CategoriaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = []
    ordering_fields = []

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(usuario=self.request.user.usuario, deleted=False, enabled=True)