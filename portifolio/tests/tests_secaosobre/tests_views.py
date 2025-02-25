import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from portifolio.models import SecaoSobre
from portifolio.views.index import PortifolioIndexTemplateView
from portifolio.views.secaosobre import (
    SecaoSobreCreateView,
    SecaoSobreDeleteView,
    SecaoSobreDetailView,
    SecaoSobreListView,
    SecaoSobreUpdateView,
)


class TestSecaoSobreViews:
    """Teste para as views do model SecaoSobre"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.secaosobre = baker.make(SecaoSobre)

    def test_secaosobre_list(self, init):
        """Teste para a view list."""
        url = reverse("portifolio:secaosobre-list")
        request = self.factory.get(url)
        request.user = self.user
        response = SecaoSobreListView.as_view()(request)
        assert response.status_code == 200

    def test_secaosobre_detail(self, init):
        """Teste para a view detail."""
        url = reverse("portifolio:secaosobre-detail", args={self.secaosobre.pk})
        request = self.factory.get(url)
        request.user = self.user
        response = SecaoSobreDetailView.as_view()(request, pk=self.secaosobre.pk)
        assert response.status_code == 200

    def test_secaosobre_create(self, init):
        """Teste para a view create."""
        url = reverse("portifolio:secaosobre-create")
        request = self.factory.get(url)
        request.user = self.user
        response = SecaoSobreCreateView.as_view()(request)
        assert response.status_code == 200

    def test_secaosobre_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("portifolio:secaosobre-create")
        request = self.factory.post(url)
        request.user = self.user
        response = SecaoSobreCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_secaosobre_update(self, init):
        """Teste para a view update."""
        url = reverse("portifolio:secaosobre-update", args={self.secaosobre.pk})
        request = self.factory.put(url)
        request.user = self.user
        response = SecaoSobreUpdateView.as_view()(request, pk=self.secaosobre.pk)
        assert response.status_code == 200

    def test_secaosobre_delete(self, init):
        """Teste para a view delete."""
        url = reverse("portifolio:secaosobre-delete", args={self.secaosobre.pk})
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = SecaoSobreDeleteView.as_view()(request, pk=self.secaosobre.pk)
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_secaosobre_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:secaosobre-list"))
        request.user = self.user
        response = SecaoSobreListView.as_view()(request)
        assert response.status_code == 200

    def test_secaosobre_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:secaosobre-list"))
        request.user = self.user
        response = SecaoSobreListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_portifolio_index(self, init):
        """Teste para a view index."""
        url = reverse("portifolio:portifolio-index")
        request = self.factory.get(url)
        request.user = self.user
        response = PortifolioIndexTemplateView.as_view()(request)
        assert response.status_code == 200
