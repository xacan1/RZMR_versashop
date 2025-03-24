from django.apps import AppConfig
from rzmr.utils import load_ru_cities


class RzmrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rzmr'
    verbose_name = 'Корпоративный сайт'
    load_ru_cities()