import pytest
from faker import Faker

from portifolio.forms.imagemheader import ImagemHeaderForm


class TestImagemHeaderForms:
    """Testes para os formulários de ImagemHeader"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_imagemheader_create(self, init):
        """Teste para criação de ImagemHeader"""
        form = ImagemHeaderForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_imagemheader_form_invalid(self, init):
        """Teste para formulário inválido de ImagemHeader"""
        form = ImagemHeaderForm(data=self.invalid_data)
        assert form.is_valid() is False
