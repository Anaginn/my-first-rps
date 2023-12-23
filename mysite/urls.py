"""Конфигурация URL-адресов mysite

Список `urlpatterns` направляет URL к представлениям.
Примеры:
Представления функций
    1. Добавьте импорт: from my_app import views
    2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Представления на основе классов
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируем функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns: path('massiv/', include('massiv.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # по любому URL-адресу, начинающемуся с admin/, Django будет находить соответствующее view (представление)
    path('', include('massiv.urls')), #Django теперь будет перенаправлять все запросы 'http://127.0.0.1:8000/' к massiv.urls
]
