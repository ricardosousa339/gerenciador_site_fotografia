import pytest
from faker import Faker

from portifolio.forms.secaocontato import SecaoContatoForm


class TestSecaoContatoForms:
    """Testes para os formulários de SecaoContato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_secaocontato_create(self, init):
        """Teste para criação de SecaoContato"""
        form = SecaoContatoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_secaocontato_form_invalid(self, init):
        """Teste para formulário inválido de SecaoContato"""
        form = SecaoContatoForm(data=self.invalid_data)
        assert form.is_valid() is False
