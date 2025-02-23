import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import Foto


class TestFotoModels:
    """Testes para o model Foto"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.foto = baker.make(Foto)

    def test_count_foto(self, init):
        """Testa a quantidade de foto"""
        assert Foto.objects.all().count() == 1

    def test_soft_delete_foto(self, init):
        """Testa o soft delete de foto"""
        Foto.objects.all().delete()
        assert Foto.objects.filter(deleted=False).count() == 0

    def test_create_foto(self, init):
        """Testa a criação de foto"""
        assert self.foto.id is not None

    def test_update_foto(self, init):
        """Testa a atualização de foto"""
        # TODO - Altere o campo e o valor
        self.foto.save()
        self.foto.campo = "valor"
        self.foto.save()
        foto = Foto.objects.get(campo="valor")
        assert foto.campo == "valor"
