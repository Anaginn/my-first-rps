import re
from django.http import JsonResponse
from django.shortcuts import render
from massiv.forms import SortedArrayForm
from massiv.models import SortedArray
import ctypes
import typing
import numpy as np


lib = ctypes.CDLL('C:\Functions.so')

def sort_array(aqs: typing.List[int]) -> ctypes.Array:
    c = len(aqs)
    lib.selectionSort.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_int, shape=(c,))
    a = (ctypes.c_int * c)(*aqs)
    res = lib.selectionSort(a, c)
    result_list = [i for i in res]
    print(result_list)
    return result_list

def selection_sort(request):
    if request.method == 'POST':
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            if 'action' in request.POST:
                array_name = form.cleaned_data['array_name']        # Получение названия массива из формы
                sorted_array = form.cleaned_data['sorted_array']    # Получение массива из формы
                res = re.findall(r'\d+', sorted_array)              # Перевод строки в числа
                intlist = list(map(int, res))                       # Перевод в лист
                arr = sort_array(intlist)               # Сортировка и возвращение результатов
                listed = ''
                for a in arr:                                   # Цикл по результату сортировки и перевод в строку для БД
                    listed += str(a) + ' '
                listed = listed[:-1]
                feed = SortedArray(                                 # Данные для сохранения в БД
                    array_name=array_name,
                    sorted_array=listed,
                )
            feed.save()
            complex = {'form': form, 'sorted_array': listed} # Данные для возвращения из функции

            return render(request, 'massiv/massiv.html', complex)


    return JsonResponse({'error': 'Invalid request'})