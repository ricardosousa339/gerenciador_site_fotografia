import pytest
from faker import Faker

from portifolio.forms.mensagemcontato import MensagemContatoForm


class TestMensagemContatoForms:
    """Testes para os formulários de MensagemContato"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_mensagemcontato_create(self, init):
        """Teste para criação de MensagemContato"""
        form = MensagemContatoForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_mensagemcontato_form_invalid(self, init):
        """Teste para formulário inválido de MensagemContato"""
        form = MensagemContatoForm(data=self.invalid_data)
        assert form.is_valid() is False
