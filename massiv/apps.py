from django.apps import AppConfig


class MassivConfig(AppConfig): # управлчет типом первичного ключа моделей, если ключ не определен, определяет первичные ключи моделей
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'massiv'
