from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Foto, ImagemHeader  # Substitua pelos seus modelos que têm campos de arquivo
from firebase_admin import storage

@receiver(post_delete, sender=Foto)
def deletar_arquivo_firebase(sender, instance, **kwargs):
    try:
        caminho = instance.arquivo.name  # adaptado para usar o nome do arquivo
        blob = storage.bucket().blob(caminho)
        blob.delete()
    except Exception as e:
        print(f"Erro ao deletar: {e}")