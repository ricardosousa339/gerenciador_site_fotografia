import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import DadosPrincipais


class TestDadosPrincipaisModels:
    """Testes para o model DadosPrincipais"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.dadosprincipais = baker.make(DadosPrincipais)

    def test_count_dadosprincipais(self, init):
        """Testa a quantidade de dadosprincipais"""
        assert DadosPrincipais.objects.all().count() == 1

    def test_soft_delete_dadosprincipais(self, init):
        """Testa o soft delete de dadosprincipais"""
        DadosPrincipais.objects.all().delete()
        assert DadosPrincipais.objects.filter(deleted=False).count() == 0

    def test_create_dadosprincipais(self, init):
        """Testa a criação de dadosprincipais"""
        assert self.dadosprincipais.id is not None

    def test_update_dadosprincipais(self, init):
        """Testa a atualização de dadosprincipais"""
        # TODO - Altere o campo e o valor
        self.dadosprincipais.save()
        self.dadosprincipais.campo = "valor"
        self.dadosprincipais.save()
        dadosprincipais = DadosPrincipais.objects.get(campo="valor")
        assert dadosprincipais.campo == "valor"
