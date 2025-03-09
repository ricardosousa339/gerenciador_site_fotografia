from django.apps import AppConfig
from base.settings import FIREBASE_CREDENTIALS
import firebase_admin
from firebase_admin import credentials

from firebase_admin import credentials

class PortifolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'portifolio'

    def ready(self):
        cred = credentials.Certificate(FIREBASE_CREDENTIALS)
        firebase_admin.initialize_app(credential=cred)
