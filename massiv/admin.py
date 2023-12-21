from django.contrib import admin
from .models import SortedArray

admin.site.register(SortedArray) # зарегистрировали нашу модель, чтобы она была доступна на странице администрирования
