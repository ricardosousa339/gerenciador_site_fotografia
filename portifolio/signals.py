from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Foto, ImagemHeader  # Substitua pelos seus modelos que têm campos de arquivo

@receiver(post_delete, sender=Foto)
def auto_delete_foto_file(sender, instance, **kwargs):
    """Exclui arquivo do Firebase Storage quando um objeto Foto é excluído"""
    if instance.arquivo:  # Note que aqui é 'arquivo', não 'imagem'
        instance.arquivo.delete(save=False)

@receiver(post_delete, sender=ImagemHeader)
def auto_delete_header_file(sender, instance, **kwargs):
    """Exclui arquivo do Firebase Storage quando um objeto ImagemHeader é excluído"""
    if instance.arquivo:
        instance.arquivo.delete(save=False)