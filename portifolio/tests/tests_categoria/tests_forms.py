import pytest
from faker import Faker

from portifolio.forms.categoria import CategoriaForm


class TestCategoriaForms:
    """Testes para os formulários de Categoria"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_categoria_create(self, init):
        """Teste para criação de Categoria"""
        form = CategoriaForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_categoria_form_invalid(self, init):
        """Teste para formulário inválido de Categoria"""
        form = CategoriaForm(data=self.invalid_data)
        assert form.is_valid() is False
