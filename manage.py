#!/usr/bin/env python
"""Утилита командной строки Django для выполнения административных задач."""
import os
import sys


def main():
    """Выполнение административных задач."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') #сообщаем какой файл настроек нужно использовать
    try:                                                               #проверяем существует ли соответствующий пакет Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, что он установлен и "
            "доступна в вашей переменной окружения PYTHONPATH? Вы "
            "забыли активировать виртуальное окружение?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
