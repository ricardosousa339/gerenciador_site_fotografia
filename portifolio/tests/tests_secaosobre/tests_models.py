import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import SecaoSobre


class TestSecaoSobreModels:
    """Testes para o model SecaoSobre"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.secaosobre = baker.make(SecaoSobre)

    def test_count_secaosobre(self, init):
        """Testa a quantidade de secaosobre"""
        assert SecaoSobre.objects.all().count() == 1

    def test_soft_delete_secaosobre(self, init):
        """Testa o soft delete de secaosobre"""
        SecaoSobre.objects.all().delete()
        assert SecaoSobre.objects.filter(deleted=False).count() == 0

    def test_create_secaosobre(self, init):
        """Testa a criação de secaosobre"""
        assert self.secaosobre.id is not None

    def test_update_secaosobre(self, init):
        """Testa a atualização de secaosobre"""
        # TODO - Altere o campo e o valor
        self.secaosobre.save()
        self.secaosobre.campo = "valor"
        self.secaosobre.save()
        secaosobre = SecaoSobre.objects.get(campo="valor")
        assert secaosobre.campo == "valor"
