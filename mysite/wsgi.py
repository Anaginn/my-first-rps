"""
Интерфейс шлюза веб -сервера (Python Web Server Gateway Interface）
Конфигурация WSGI для проекта mysite.

Он раскрывает вызываемый WSGI объект как переменную уровня модуля с именем ``application''.
Используется для соединения между веб -сервером и веб -приложением (Framework).
"""

import os

from django.core.wsgi import get_wsgi_application

#загружаем переменные окружения из файла .env (если такой есть)
# и устанавливаем имя файла с настройками Django через переменную DJANGO_SETTINGS_MODULE.
# Далее мы создаем объект application, используя функцию get_asgi_application из модуля
# django.core.asgi.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
