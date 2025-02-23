import pytest
from faker import Faker

from portifolio.forms.foto import FotoForm


class TestFotoForms:
    """Testes para os formulários de Foto"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_foto_create(self, init):
        """Teste para criação de Foto"""
        form = FotoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_foto_form_invalid(self, init):
        """Teste para formulário inválido de Foto"""
        form = FotoForm(data=self.invalid_data)
        assert form.is_valid() is False
