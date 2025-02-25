import pytest
from faker import Faker

from portifolio.forms.fatosobre import FatoSobreForm


class TestFatoSobreForms:
    """Testes para os formulários de FatoSobre"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_fatosobre_create(self, init):
        """Teste para criação de FatoSobre"""
        form = FatoSobreForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_fatosobre_form_invalid(self, init):
        """Teste para formulário inválido de FatoSobre"""
        form = FatoSobreForm(data=self.invalid_data)
        assert form.is_valid() is False
