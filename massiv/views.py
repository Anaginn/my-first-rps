import sys
import re
from django.http import JsonResponse
from massiv.models import SortedArray
from django.shortcuts import render, get_object_or_404
from .forms import SortedArrayForm
from django.shortcuts import redirect



def selectionSort(sortArray): # Функция сортировки
    minI = 0
    success=True
    try:  # Функция проверки верного отрабатывания функции
        for i in range(len(sortArray)):  # Цикл по всему массиву
            min = sys.maxsize    # Инициализация макс числа для сравнений
            for j in range(i, len(sortArray)): # Цикл по подмассиву
                if sortArray[j] < min:   # Если элемент меньше минимального
                    min = sortArray[j]   # Замена минимального элемента
                    minI = j            # Сохранение индекса минимального элемента
            if sortArray[minI] != sortArray[i]:     # Проверка, что элемент не стоит на своём месте
                sortArray[minI], sortArray[i] = sortArray[i], sortArray[minI]   # Перестановка
    except:
        success=False
    complex = (sortArray,  success) # Возвращение из функции массива и успешности отрабатывания
    return complex


def index(request): #функция которая принимает в качестве аргумента request (всё, что мы получим от пользователя в качестве запроса через Интернет)
    array = SortedArray.objects.all()[:100] #с помощью QuerySet(список объектов заданной модели, который позволяет читать данные из бд) отображаем на странице все масиивы
    return render(request, 'massiv/index.html', {'array': array}) # отображает переменные {'array': array} в шаблоне 'massiv/index.html'

def sort_array(request):
    if request.method == 'POST':
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            if 'action' in request.POST:
                array_name = form.cleaned_data['array_name']        # Получение названия массива из формы
                sorted_array = form.cleaned_data['sorted_array']    # Получение массива из формы
                res = re.findall(r'\d+', sorted_array)              # Перевод строки в числа
                intlist = list(map(int, res))                       # Перевод в лист
                arr, success = selectionSort(intlist)               # Сортировка и возвращение результатов
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



def post_detail(request, pk):
    post = get_object_or_404(SortedArray, pk=pk) #если нет поста с нужным номером, то будет ошибка, что его не существует, вместо другой страшной ошибки
    return render(request, 'massiv/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST": # ситуация когда мы хотим получить данные от пользователя
        form = SortedArrayForm(request.POST) # создаем форму с этими данными
        if form.is_valid(): # проверка коректности формы (все ли поля заполнены)
            post = form.save() # сохранение формы
            return redirect('post_detail', pk=post.pk) # переадресация на другую страницу
    else:
        form = SortedArrayForm() # ситуация когда мы зашли на страницу и мы видим пустую форму
    return render(request, 'massiv/post_edit.html', {'form': form}) # отображение переменных в шаблоне


def post_edit(request, pk):
    post = get_object_or_404(SortedArray, pk=pk) # получаем модель для редактирования
    if request.method == "POST":
        form = SortedArrayForm(request.POST, instance=post) # создаем форму с данными и передаем post форме
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = SortedArrayForm(instance=post) # ситуация когда мы зашли на страницу для редактирования
    return render(request, 'massiv/post_edit.html', {'form': form})

