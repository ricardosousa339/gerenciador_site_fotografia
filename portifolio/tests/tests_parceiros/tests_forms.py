import pytest
from faker import Faker

from portifolio.forms.parceiros import ParceirosForm


class TestParceirosForms:
    """Testes para os formulários de Parceiros"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_parceiros_create(self, init):
        """Teste para criação de Parceiros"""
        form = ParceirosForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_parceiros_form_invalid(self, init):
        """Teste para formulário inválido de Parceiros"""
        form = ParceirosForm(data=self.invalid_data)
        assert form.is_valid() is False
