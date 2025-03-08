import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import SecaoContato


class TestSecaoContatoModels:
    """Testes para o model SecaoContato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.secaocontato = baker.make(SecaoContato)

    def test_count_secaocontato(self, init):
        """Testa a quantidade de secaocontato"""
        assert SecaoContato.objects.all().count() == 1

    def test_soft_delete_secaocontato(self, init):
        """Testa o soft delete de secaocontato"""
        SecaoContato.objects.all().delete()
        assert SecaoContato.objects.filter(deleted=False).count() == 0

    def test_create_secaocontato(self, init):
        """Testa a criação de secaocontato"""
        assert self.secaocontato.id is not None

    def test_update_secaocontato(self, init):
        """Testa a atualização de secaocontato"""
        # TODO - Altere o campo e o valor
        self.secaocontato.save()
        self.secaocontato.campo = "valor"
        self.secaocontato.save()
        secaocontato = SecaoContato.objects.get(campo="valor")
        assert secaocontato.campo == "valor"
