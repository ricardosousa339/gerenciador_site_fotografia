from django.db import models
from django.conf import settings

from core.models import Base
from portifolio.files import generate_unique_file_name
from portifolio.validators import FileSizeValidator
from django.core.validators import FileExtensionValidator
from usuario.models import Usuario

class Album(Base):
    titulo = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='albums'
    )
    capa = models.ForeignKey(
        "Foto",
        on_delete=models.SET_NULL,
        related_name='cover',
        blank=True,
        null=True
    )
    fotos = models.ManyToManyField(
        "Foto",
        related_name='album'
    )

    
    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbuns"
        fields_display = ["titulo", "usuario", "url"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.titulo


class Foto(Base):
    nome = models.CharField(max_length=255)
    arquivo = models.ImageField(
        "Arquivo",
        upload_to=generate_unique_file_name,
        blank=True,
        null=True,
        help_text="Arquivo da foto",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            FileSizeValidator(max_size=5),
        ],
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='fotos'
    )

    
    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        fields_display = ["nome"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.nome
    
class ImagemHeader(Base):
    imagem = models.ForeignKey(
        Foto,
        on_delete=models.CASCADE,
        related_name='header'
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='headers'
    )

    class Meta:
        verbose_name = "Imagem de Cabeçalho"
        verbose_name_plural = "Imagens de Cabeçalho"
        fields_display = ["imagem"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.imagem.nome 