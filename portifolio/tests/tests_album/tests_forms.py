import pytest
from faker import Faker

from portifolio.forms.album import AlbumForm


class TestAlbumForms:
    """Testes para os formulários de Album"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker()
        # TODO - Adicione campos
        self.valid_data = {}
        self.invalid_data = {}

    def test_album_create(self, init):
        """Teste para criação de Album"""
        form = AlbumForm(data=self.valid_data)
        assert form.is_valid() is True

    def teste_album_form_invalid(self, init):
        """Teste para formulário inválido de Album"""
        form = AlbumForm(data=self.invalid_data)
        assert form.is_valid() is False
