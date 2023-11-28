from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from .models import SortedArray


def index(request):
    return render(request, 'massiv/index.html', {})


def sort_array(request):
    if request.method == 'POST':
        array_to_sort = request.POST.getlist('array[]')
        # Отправить массив на обработку на C++ и получить отсортированный массив

        # Здесь должен быть код вызова функции на C++, например:
        # sorted_array = call_cpp_sort_function(array_to_sort)

        sorted_array = sorted(array_to_sort)  # Временное решение, сортировка на Python

        # Сохранение отсортированного массива в файл
        with open('sorted_array.txt', 'w') as file:
            for element in sorted_array:
                file.write(str(element) + '\n')

        # Сохранение отсортированного массива в базе данных
        sorted_array_str = ','.join(sorted_array)
        SortedArray.objects.create(array_name='Sorted Array', sorted_array=sorted_array_str)

        return JsonResponse({'sorted_array': sorted_array})

    return JsonResponse({'error': 'Invalid request'})
