from django import forms

from .models import SortedArray

class SortedArrayForm(forms.ModelForm):

    class Meta:
        model = SortedArray  # определяем, какая модель будет использоваться для создания формы
        fields = ('array_name', 'sorted_array')  # какие поля там будут