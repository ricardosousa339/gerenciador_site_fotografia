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
        null=True,
        help_text="A foto que será a capa do álbum",
    )
    fotos = models.ManyToManyField(
        "Foto",
        related_name='album',
        help_text="Crie as Fotos e elas aparecerão aqui pra serem selecionadas",
    )
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.SET_NULL,
        related_name='albums',
        blank=True,
        null=True,
        help_text="Crie as Categorias e elas aparecerão aqui pra serem selecionadas",
    )

    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbuns"
        fields_display = ["titulo", "url", "categoria"]
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
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "svg"]),
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
    
class DadosPrincipais(Base):
    nome = models.CharField(
        max_length=255,
        help_text="Seu nome")
    subtitulo = models.TextField(
        max_length=1000,
        help_text="Texto embaixo do seu nome"
    )

    titulo_portifolio = models.CharField(
        "Título do Portifólio",
        max_length=255,
        help_text="Ficará acima dos álbums",
        blank=True,
        null=True
    )
    descricao_portifolio = models.TextField(
        "Descrição do Portifólio",
        max_length=1000,
        help_text="Texto embaixo do título do portifólio",
        blank=True,
        null=True
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='dados_principais'
    )

    class Meta:
        verbose_name = "Dados Principais"
        verbose_name_plural = "Dados Dados Principais"
        fields_display = ["nome", "subtitulo"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.nome
    
class SecaoContato(Base):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(
        max_length=1000,
        help_text="Texto da Seção Contato"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='secoes_contato'
    )

    class Meta:
        verbose_name = "Seção Contato"
        verbose_name_plural = "Seções Contato"
        fields_display = ["titulo", "descricao"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.titulo

class ImagemHeader(Base):
    imagem = models.ForeignKey(
        Foto,
        on_delete=models.CASCADE,
        related_name='header',
        help_text="Você deve criar uma foto então poderá selecioná-la aqui, para ficar em destaque"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='headers'
    )

    class Meta:
        verbose_name = "Imagens em Destaque"
        verbose_name_plural = "Imagens em Destaque"
        fields_display = ["imagem"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.imagem.nome 


class Categoria(Base):
    nome = models.CharField(max_length=255)
    icone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Nome do ícone Lucide (https://lucide.dev)"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='categorias',
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        fields_display = ["nome", "icone"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.nome


class SecaoSobre(Base):
    titulo = models.CharField(
        max_length=255,
        help_text="Ex.: Sobre Mim")
    descricao = models.TextField(
        max_length=1000,
        help_text="Texto da Seção Sobre"
    )
    
    imagem = models.ForeignKey(
        Foto,
        on_delete=models.SET_NULL,
        related_name='secao_sobre',
        blank=True,
        null=True,
        help_text="Imagem da seção"
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='secoes_sobre'
    )
    fatos_sobre = models.ManyToManyField(
        "FatoSobre",
        related_name='secoes_sobre_many',
        help_text="Crie os Fatos Sobre e eles aparecerão aqui pra serem selecionados"
    )

    class Meta:
        verbose_name = "Seção Sobre"
        verbose_name_plural = "Seções Sobre"
        fields_display = ["titulo"]
        # icon_model = "fas fa-user"

class FatoSobre(Base):
    icone = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Nome do ícone Lucide (https://lucide.dev)"
    )
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='fatos_sobre',
    )
    class Meta:
        verbose_name = "Fato Sobre"
        verbose_name_plural = "Fato Sobre"
        fields_display = ["titulo", "subtitulo"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.titulo + " - " + self.subtitulo

class MensagemContato(Base):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='mensagens'
    )

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        fields_display = ["nome", "email"]
        # icon_model = "fas fa-user"

    def __str__(self):
        return self.nome
    
class Parceiros(Base):
    nome = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    logo = models.ForeignKey(
        Foto,
        on_delete=models.SET_NULL,
        related_name='parceiros',
        blank=True,
        null=True
    )
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='parceiros'
    )

    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
        fields_display = ["nome", "url"]
        # icon_model = "fas fa-user"

    #TODO: Ampliar pra postar projetos de desenvolvimento