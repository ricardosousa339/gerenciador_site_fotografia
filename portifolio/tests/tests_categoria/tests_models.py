import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import Categoria


class TestCategoriaModels:
    """Testes para o model Categoria"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.categoria = baker.make(Categoria)

    def test_count_categoria(self, init):
        """Testa a quantidade de categoria"""
        assert Categoria.objects.all().count() == 1

    def test_soft_delete_categoria(self, init):
        """Testa o soft delete de categoria"""
        Categoria.objects.all().delete()
        assert Categoria.objects.filter(deleted=False).count() == 0

    def test_create_categoria(self, init):
        """Testa a criação de categoria"""
        assert self.categoria.id is not None

    def test_update_categoria(self, init):
        """Testa a atualização de categoria"""
        # TODO - Altere o campo e o valor
        self.categoria.save()
        self.categoria.campo = "valor"
        self.categoria.save()
        categoria = Categoria.objects.get(campo="valor")
        assert categoria.campo == "valor"
