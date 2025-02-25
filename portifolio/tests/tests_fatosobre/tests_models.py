import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import FatoSobre


class TestFatoSobreModels:
    """Testes para o model FatoSobre"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.fatosobre = baker.make(FatoSobre)

    def test_count_fatosobre(self, init):
        """Testa a quantidade de fatosobre"""
        assert FatoSobre.objects.all().count() == 1

    def test_soft_delete_fatosobre(self, init):
        """Testa o soft delete de fatosobre"""
        FatoSobre.objects.all().delete()
        assert FatoSobre.objects.filter(deleted=False).count() == 0

    def test_create_fatosobre(self, init):
        """Testa a criação de fatosobre"""
        assert self.fatosobre.id is not None

    def test_update_fatosobre(self, init):
        """Testa a atualização de fatosobre"""
        # TODO - Altere o campo e o valor
        self.fatosobre.save()
        self.fatosobre.campo = "valor"
        self.fatosobre.save()
        fatosobre = FatoSobre.objects.get(campo="valor")
        assert fatosobre.campo == "valor"
