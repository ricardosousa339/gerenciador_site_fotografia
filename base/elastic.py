from decouple import config

APP_ID = "gerenciador_de_site_de_fotografia"

ELASTIC_APM = {
    "SERVICE_NAME": "gerenciador_de_site_de_fotografia",
    "SERVER_URL": config("ELASTIC_APM_SERVER_URL"),
    "DEBUG": config("DEBUG", default=False, cast=bool),
    "ENVIRONMENT": config("ENVIRONMENT", default="desenvolvimento"),
}