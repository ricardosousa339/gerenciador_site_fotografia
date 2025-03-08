import pytest
from faker import Faker

from portifolio.forms.dadosprincipais import DadosPrincipaisForm


class TestDadosPrincipaisForms:
    """Testes para os formulários de DadosPrincipais"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_dadosprincipais_create(self, init):
        """Teste para criação de DadosPrincipais"""
        form = DadosPrincipaisForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_dadosprincipais_form_invalid(self, init):
        """Teste para formulário inválido de DadosPrincipais"""
        form = DadosPrincipaisForm(data=self.invalid_data)
        assert form.is_valid() is False
