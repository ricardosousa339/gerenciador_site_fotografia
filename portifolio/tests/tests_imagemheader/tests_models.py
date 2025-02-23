import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import ImagemHeader


class TestImagemHeaderModels:
    """Testes para o model ImagemHeader"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.imagemheader = baker.make(ImagemHeader)

    def test_count_imagemheader(self, init):
        """Testa a quantidade de imagemheader"""
        assert ImagemHeader.objects.all().count() == 1

    def test_soft_delete_imagemheader(self, init):
        """Testa o soft delete de imagemheader"""
        ImagemHeader.objects.all().delete()
        assert ImagemHeader.objects.filter(deleted=False).count() == 0

    def test_create_imagemheader(self, init):
        """Testa a criação de imagemheader"""
        assert self.imagemheader.id is not None

    def test_update_imagemheader(self, init):
        """Testa a atualização de imagemheader"""
        # TODO - Altere o campo e o valor
        self.imagemheader.save()
        self.imagemheader.campo = "valor"
        self.imagemheader.save()
        imagemheader = ImagemHeader.objects.get(campo="valor")
        assert imagemheader.campo == "valor"
