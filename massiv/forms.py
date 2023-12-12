from django import forms

from .models import SortedArray

class SortedArrayForm(forms.ModelForm):

    class Meta:
        model = SortedArray
        fields = ('array_name', 'sorted_array')