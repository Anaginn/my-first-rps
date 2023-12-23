"""
Асинхронный интерфейс шлюза (Asynchronous Server Gateway Interface）
Конфигурация ASGI для проекта mysite.

Он раскрывает вызываемую ASGI-систему как переменную уровня модуля с именем ``application''.
расширенная версия WSGI, которая направлена ​​на предоставление стандарта для веб -службы, структуры и приложений Python
"""

import os

from django.core.asgi import get_asgi_application

# загружаем переменные окружения из файла .env (если такой есть)
# и устанавливаем имя файла с настройками Django через переменную DJANGO_SETTINGS_MODULE.
# Далее мы создаем объект application, используя функцию get_asgi_application из модуля
# django.core.asgi.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
