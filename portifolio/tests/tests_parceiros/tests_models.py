import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import Parceiros


class TestParceirosModels:
    """Testes para o model Parceiros"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.parceiros = baker.make(Parceiros)

    def test_count_parceiros(self, init):
        """Testa a quantidade de parceiros"""
        assert Parceiros.objects.all().count() == 1

    def test_soft_delete_parceiros(self, init):
        """Testa o soft delete de parceiros"""
        Parceiros.objects.all().delete()
        assert Parceiros.objects.filter(deleted=False).count() == 0

    def test_create_parceiros(self, init):
        """Testa a criação de parceiros"""
        assert self.parceiros.id is not None

    def test_update_parceiros(self, init):
        """Testa a atualização de parceiros"""
        # TODO - Altere o campo e o valor
        self.parceiros.save()
        self.parceiros.campo = "valor"
        self.parceiros.save()
        parceiros = Parceiros.objects.get(campo="valor")
        assert parceiros.campo == "valor"
