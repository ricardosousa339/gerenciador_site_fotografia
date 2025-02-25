import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import MensagemContato


class TestMensagemContatoModels:
    """Testes para o model MensagemContato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.mensagemcontato = baker.make(MensagemContato)

    def test_count_mensagemcontato(self, init):
        """Testa a quantidade de mensagemcontato"""
        assert MensagemContato.objects.all().count() == 1

    def test_soft_delete_mensagemcontato(self, init):
        """Testa o soft delete de mensagemcontato"""
        MensagemContato.objects.all().delete()
        assert MensagemContato.objects.filter(deleted=False).count() == 0

    def test_create_mensagemcontato(self, init):
        """Testa a criação de mensagemcontato"""
        assert self.mensagemcontato.id is not None

    def test_update_mensagemcontato(self, init):
        """Testa a atualização de mensagemcontato"""
        # TODO - Altere o campo e o valor
        self.mensagemcontato.save()
        self.mensagemcontato.campo = "valor"
        self.mensagemcontato.save()
        mensagemcontato = MensagemContato.objects.get(campo="valor")
        assert mensagemcontato.campo == "valor"
