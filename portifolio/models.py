from django.db import models
from django.conf import settings

from core.models import Base
from usuario.models import Usuario

class Album(Base):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='albums'
    )

    
    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbuns"
        fields_display = ["titulo", "usuario"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.title

class Foto(Base):
    nome = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    
    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        fields_display = ["nome", "url", "album"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.name