import pytest
from faker import Faker

from portifolio.forms.secaosobre import SecaoSobreForm


class TestSecaoSobreForms:
    """Testes para os formulários de SecaoSobre"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_secaosobre_create(self, init):
        """Teste para criação de SecaoSobre"""
        form = SecaoSobreForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_secaosobre_form_invalid(self, init):
        """Teste para formulário inválido de SecaoSobre"""
        form = SecaoSobreForm(data=self.invalid_data)
        assert form.is_valid() is False
