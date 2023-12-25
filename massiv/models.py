from django.db import models


class SortedArray(models.Model):          #эта строка определяет нашу модель (объект), так Django поймет, что он должен сохранить ее в базу данных
    array_name = models.CharField(max_length=100) #так мы определяем текстовое поле с ограничением на количество символов.
    sorted_array = models.TextField() #так определяется поле для неограниченно длинного текста

