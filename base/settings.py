import os
import sys
from datetime import timedelta

import sentry_sdk
from decouple import Csv, config
from django.contrib.messages import constants as messages
from sentry_sdk.integrations.django import DjangoIntegration
from google.oauth2 import service_account

# Set Google credentials path explicitly in the environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
    'firebase-key.json'
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "usuario",
    "configuracao_core",
    # "atendimento",
    "tempus_dominus",
    # Django Rest Framework
    "drf_spectacular",
    "dj_rest_auth",
    "rest_framework",
    "rest_framework.authtoken",
    "portifolio",
    "corsheaders",
    # Apps do projeto
]


FASTAPI_APPS = []

# Apps que não devem ser renderizadas no menu
IGNORED_APPS = []

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.header_control.HeaderControlMiddleware",
    "core.middleware.current_user.CurrentUserMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "base.urls"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MESSAGE_TAGS = {
    messages.DEBUG: "info",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger",
}

WSGI_APPLICATION = "base.wsgi.application"

# TODO: Alterar as configurações do banco de dados no arquivo .env
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-BR"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DECIMAL_SEPARATOR = ","
USE_THOUSAND_SEPARATOR = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

PROJECT_NAME = "Gerenciador de Site de Fotografia"

# Lista de apps que devem ser mapeadas para gerar a documentação via Sphinxs
DOC_APPS = ["usuario", "configuracao_core"]

# Desativando as migrações quando estiver executando os testes.
if "test" in sys.argv and DEBUG is True:

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "TEST": {"NAME": "test.sqlite3"},
        }
    }

    MIGRATION_MODULES = DisableMigrations()

if DEBUG:
    INSTALLED_APPS.append("django_extensions")
    # Adicionando o debug tool bar no middleware
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    # MIDDLEWARE.append('silk.middleware.SilkyMiddleware')
    # Adicionando o debug tool bar no installed apps
    INSTALLED_APPS.append("debug_toolbar")
    # INSTALLED_APPS.append('silk')
    # Configurando o debug tool bar para mapear os eventos do localhost
    INTERNAL_IPS = ["127.0.0.1", "localhost"]

# Django Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 200,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# DRF JWT
SIMPLE_JWT = {
    # Configurando para o Token expirar de hora em hora
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    # Configurando para o Refresh Token expirar a cada dia.
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# ÁREA PARA CONFIGURAÇÃO DAS VARIÁVEIS DO PROJETO
SYSTEM_NAME = "Gerenciador De Site De Fotografia "

LOGIN_URL = "/core/login"
LOGIN_REDIRECT_URL = "/core"
LOGOUT_REDIRECT_URL = "/core/login"

"""
Variável responsável por configurar qual Manager utilizar.
Se for True usa o manager padrão que retorna todos os  elementos mesmo os marcados com deleted = True e enabled = True
Se for False usa o manager configurado para não mostrar os elementos marcados com deleted = True e enabled = False
"""
USE_DEFAULT_MANAGER = False

"""
Variável responsável por configurar ser será gerada auditoria para as operações de inserção exclusão e alteração
dos models que herdarem de base.
"""
AUDIT_ENABLED = True

DELETED_MANY_TO_MANY = True

# O Valor dessa variável não deve ser alterado
FLUTTER_PROJECT_PATH = "../../Flutter/"

FLUTTER_APPS = [
    "usuario",
]

FASTAPI_URL = config("FASTAPI_URL", "")
FASTAPI_USER_BG_TASKS = config("FASTAPI_USER_BG_TASKS", "")
FASTAPI_KEY_BG_TASKS = config("FASTAPI_KEY_BG_TASKS", "")

# Usados apenas para desenvolvimento do Flutter
FLUTTER_API_USER_DEV = config("FLUTTER_API_USER_DEV", "")
FLUTTER_API_PASSWORD_DEV = config("FLUTTER_API_PASSWORD_DEV", "")
API_PATH = config("API_PATH", "")
API_PASSWORD_DEV = config("SENHA_PADRAO", default="")
API_USER_DEV = config("USUARIO_PADRAO", default="admin")
ORGANIZATION_FLUTTER_NAME = config("ORGANIZATION_FLUTTER_NAME", default="agtec_core")

PATH_PRODUCTION = config("PATH_PRODUCTION", default="")

FLUTTER_API_PATH = config("FLUTTER_API_PATH", "")
IP_ADDRESS_DEFAULT_FLUTTER = config("IP_ADDRESS_DEFAULT_FLUTTER", "")

"""
Configuração para o Middleware Header_control
O middleware header_control é responsavel por controlar
Se o componente header do agtec_core vai ser renderizado ou não
"""
# Middleware Header Control
HEADER_COMPLETO = True
HEADER_ACTIONS = True
HEADER_VERTICAL = True
BREAD_CRUMBS = True
# Fim da configuração do Middleware Header Control

if DEBUG is False:
    sentry_sdk.init(
        dsn=config("SENTRY_DNS"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
        environment=config("ENVIRONMENT", default="desenvolvimento"),
    )

    from .elastic import ELASTIC_APM

    ELASTIC_APM
    INSTALLED_APPS.append("elasticapm.contrib.django")
    MIDDLEWARE.append("elasticapm.contrib.django.middleware.TracingMiddleware")


TEMPUS_DOMINUS_LOCALIZE = True
TEMPUS_DOMINUS_INCLUDE_ASSETS = True
TEMPUS_DOMINUS_DATE_FORMAT = "DD/MM/YYYY"
TEMPUS_DOMINUS_TIME_FORMAT = "HH:mm"

# Campo primary auto create
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Copyright
COPYRIGHT = "Mateus Machado"
WEBHOOK_DEPLOY_TOKEN = config("DEPLOY_TOKEN")
# Emails
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_TIMEOUT = config("EMAIL_TIMEOUT", default=10, cast=int)

# Configuração de armazenamento condicional
# Detecta se estamos rodando testes
RUNNING_TESTS = 'test' in sys.argv

# Force local storage for tests, otherwise use config
USE_FIREBASE_STORAGE = False if RUNNING_TESTS else config('USE_FIREBASE_STORAGE', default=not DEBUG, cast=bool)

if USE_FIREBASE_STORAGE:
    # Firebase Storage para produção
    FIREBASE_CREDENTIALS = os.path.join(BASE_DIR, 'firebase-key.json')
    # Verificar se o arquivo existe antes de tentar usá-lo
    if os.path.exists(FIREBASE_CREDENTIALS):
        DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
        GS_BUCKET_NAME = config('GS_BUCKET_NAME')
        GS_PROJECT_ID = config('GS_PROJECT_ID')
        GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
            FIREBASE_CREDENTIALS
        )
    else:
        # Fallback para storage local se o arquivo de credenciais não existir
        DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
        import warnings
        warnings.warn(
            f"Firebase credentials file not found at {FIREBASE_CREDENTIALS}. "
            "Using local file storage instead."
        )
else:
    # Armazenamento local para desenvolvimento e testes
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    # Os arquivos serão armazenados na pasta MEDIA_ROOT configurada anteriormente

# Swagger e Redoc
SPECTACULAR_SETTINGS = {
    "TITLE": "Gerenciador de Site de Fotografia API",
    "DESCRIPTION": "Swagger do Projeto Gerenciador De Site De Fotografia API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "LICENSE": {
        "name": "BSD License",
        "url": "https://www.palmas.to.gov.br/",
    },
    "CONTACT": {
        "name": "Ricardo Henrique",
        "email": "dev.ricardohenrique@gmail.com",
    },
    "TOS": "https://www.ricardomachado.me/",
    "SERVE_PERMISSIONS": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.IsAdminUser",
    ],
}
