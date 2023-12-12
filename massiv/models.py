from django.db import models


class SortedArray(models.Model):
    array_name = models.CharField(max_length=100)
    sorted_array = models.TextField()

    def __str__(self):
        return self.array_name
