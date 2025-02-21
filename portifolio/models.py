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
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.SET_NULL,
        related_name='albums',
        blank=True,
        null=True
    )
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

    
    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbuns"
        fields_display = ["titulo", "usuario", "url", "categoria"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.title

class Categoria(Base):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        fields_display = ["nome", "usuario"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.name
class Foto(Base):
    nome = models.CharField(max_length=255)
    arquivo = models.ImageField(
        "Arquivo",
        upload_to=generate_unique_file_name,
        blank=True,
        null=True,
        help_text="Arquivo da foto",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg", "png"]),
            FileSizeValidator(max_size=5),
        ],
    )

    
    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        fields_display = ["nome", "url", "album"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.name
    
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
        fields_display = ["imagem", "usuario"]
        # icon_model = "fas fa-user"