import pytest
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory
from django.urls import reverse
from faker import Faker
from model_bakery import baker

from portifolio.models import MensagemContato
from portifolio.views.index import PortifolioIndexTemplateView
from portifolio.views.mensagemcontato import (
    MensagemContatoCreateView,
    MensagemContatoDeleteView,
    MensagemContatoDetailView,
    MensagemContatoListView,
    MensagemContatoUpdateView,
)


class TestMensagemContatoViews:
    """Teste para as views do model MensagemContato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="teste",
            email="teste@email.com.br",
            password="senha_padrao_deve_ser_mudada",
        )
        self.mensagemcontato = baker.make(MensagemContato)

    def test_mensagemcontato_list(self, init):
        """Teste para a view list."""
        url = reverse("portifolio:mensagemcontato-list")
        request = self.factory.get(url)
        request.user = self.user
        response = MensagemContatoListView.as_view()(request)
        assert response.status_code == 200

    def test_mensagemcontato_detail(self, init):
        """Teste para a view detail."""
        url = reverse(
            "portifolio:mensagemcontato-detail", args={self.mensagemcontato.pk}
        )
        request = self.factory.get(url)
        request.user = self.user
        response = MensagemContatoDetailView.as_view()(
            request, pk=self.mensagemcontato.pk
        )
        assert response.status_code == 200

    def test_mensagemcontato_create(self, init):
        """Teste para a view create."""
        url = reverse("portifolio:mensagemcontato-create")
        request = self.factory.get(url)
        request.user = self.user
        response = MensagemContatoCreateView.as_view()(request)
        assert response.status_code == 200

    def test_mensagemcontato_create_post(self, init):
        """Teste para a view create usando Post."""

        # TODO - Adicione campos
        data = {}
        url = reverse("portifolio:mensagemcontato-create")
        request = self.factory.post(url)
        request.user = self.user
        response = MensagemContatoCreateView.as_view()(request, data=data)
        assert response.status_code == 200

    def test_mensagemcontato_update(self, init):
        """Teste para a view update."""
        url = reverse(
            "portifolio:mensagemcontato-update", args={self.mensagemcontato.pk}
        )
        request = self.factory.put(url)
        request.user = self.user
        response = MensagemContatoUpdateView.as_view()(
            request, pk=self.mensagemcontato.pk
        )
        assert response.status_code == 200

    def test_mensagemcontato_delete(self, init):
        """Teste para a view delete."""
        url = reverse(
            "portifolio:mensagemcontato-delete", args={self.mensagemcontato.pk}
        )
        request = self.factory.delete(url)
        setattr(request, "session", "session")
        messages = FallbackStorage(request)
        setattr(request, "_messages", messages)
        request.user = self.user
        response = MensagemContatoDeleteView.as_view()(
            request, pk=self.mensagemcontato.pk
        )
        mensagem = list(messages)[0].extra_tags
        assert mensagem == "success"
        assert response.status_code == 302

    def test_mensagemcontato_queryset_superuser_status(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:mensagemcontato-list"))
        request.user = self.user
        response = MensagemContatoListView.as_view()(request)
        assert response.status_code == 200

    def test_mensagemcontato_queryset_superuser(self, init, client):
        """Retornar o status code 200 ao verificar itens cadastrados a partir do superuser logado"""
        client.force_login(self.user)
        request = self.factory.get(reverse("portifolio:mensagemcontato-list"))
        request.user = self.user
        response = MensagemContatoListView.as_view()(request)
        assert len(response.context_data["object_list"]) == 1

    def test_portifolio_index(self, init):
        """Teste para a view index."""
        url = reverse("portifolio:portifolio-index")
        request = self.factory.get(url)
        request.user = self.user
        response = PortifolioIndexTemplateView.as_view()(request)
        assert response.status_code == 200
