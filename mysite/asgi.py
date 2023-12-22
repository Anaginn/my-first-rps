"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#загружаем переменные окружения из файла .env (если такой есть) и устанавливаем имя файла с настройками Django через переменную DJANGO_SETTINGS_MODULE. Далее мы создаем объект application, используя функцию get_asgi_application из модуля django.core.asgi.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
