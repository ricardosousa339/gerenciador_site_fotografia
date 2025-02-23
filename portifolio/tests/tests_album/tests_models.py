import pytest
from faker import Faker
from model_bakery import baker

from portifolio.models import Album


class TestAlbumModels:
    """Testes para o model Album"""

    @pytest.fixture
    def init(self, db):
        self.faker = Faker("pt_BR")
        self.album = baker.make(Album)

    def test_count_album(self, init):
        """Testa a quantidade de album"""
        assert Album.objects.all().count() == 1

    def test_soft_delete_album(self, init):
        """Testa o soft delete de album"""
        Album.objects.all().delete()
        assert Album.objects.filter(deleted=False).count() == 0

    def test_create_album(self, init):
        """Testa a criação de album"""
        assert self.album.id is not None

    def test_update_album(self, init):
        """Testa a atualização de album"""
        # TODO - Altere o campo e o valor
        self.album.save()
        self.album.campo = "valor"
        self.album.save()
        album = Album.objects.get(campo="valor")
        assert album.campo == "valor"
