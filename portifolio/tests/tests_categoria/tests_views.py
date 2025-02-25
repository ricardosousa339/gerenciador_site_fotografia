import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from portifolio.models import Categoria
from portifolio.views.categoria import (
    CategoriaCreateView,
    CategoriaDeleteView,
    CategoriaDetailView,
    CategoriaListView,
    CategoriaUpdateView,
)
from portifolio.views.index import PortifolioIndexTemplateView


class TestCategoriaViews:
    """Teste para as views do model Categoria"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.categoria = baker.make(Categoria)

    def test_categoria_list(self, init):
        """Teste para a view list."""
        url = reverse("portifolio:categoria-list")
        request = self.factory.get(url)
        request.user = self.user
        response = CategoriaListView.as_view()(request)
        assert response.status_code == 200

    def test_categoria_detail(self, init):
        """Teste para a view detail."""
        url = reverse("portifolio:categoria-detail", args={self.categoria.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = CategoriaDetailView.as_view()(request, pk=self.categoria.pk)
        assert response.status_code == 200

    def test_categoria_create(self, init):
        """Teste para a view create."""
        url = reverse("portifolio:categoria-create")
        request = self.factory.get(url)
        request.user = self.user
        response = CategoriaCreateView.as_view()(request)
        assert response.status_code == 200

    def test_categoria_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("portifolio:categoria-create")
        request = self.factory.post(url)
        request.user = self.user
        response = CategoriaCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_categoria_update(self, init):
        """Teste para a view update."""
        url = reverse("portifolio:categoria-update", args={self.categoria.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = CategoriaUpdateView.as_view()(request, pk=self.categoria.pk)
        assert response.status_code == 200

    def test_categoria_delete(self, init):
        """Teste para a view delete."""
        url = reverse("portifolio:categoria-delete", args={self.categoria.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = CategoriaDeleteView.as_view()(request, pk=self.categoria.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_categoria_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:categoria-list"))
        request.user = self.user
        response = CategoriaListView.as_view()(request)
        assert response.status_code == 200

    def test_categoria_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:categoria-list"))
        request.user = self.user
        response = CategoriaListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_portifolio_index(self, init):
        """Teste para a view index."""
        url = reverse("portifolio:portifolio-index")
        request = self.factory.get(url)
        request.user = self.user
        response = PortifolioIndexTemplateView.as_view()(request)
        assert response.status_code == 200
