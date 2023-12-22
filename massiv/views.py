import sys
import time
import random
from django.http import JsonResponse
from massiv.models import SortedArray
from django.shortcuts import render, get_object_or_404
from .forms import SortedArrayForm
from django.shortcuts import redirect



def selectionSort(sortArray):
    minI = 0
    success = True
    try:
        for i in range(len(sortArray)):
            min = sys.maxsize
            for j in range(i, len(sortArray)):
                if sortArray[j] < min:
                    min = sortArray[j]
                    minI = j
            if sortArray[minI] != sortArray[i]:
                sortArray[minI], sortArray[i] = sortArray[i], sortArray[minI]
    except:
        success = False
    complex = (sortArray, success)
    return complex

def FillDataBase(count, timeWork):
    maxSize = 10
    start = time.clock()
    a = []
    for i in range(count):
        size = random.randint(0, maxSize)
        for j in range(size):
            a[j] = random.randint(0, maxSize)

    end = time.clock()
    timeWork = (end - start) / time.process_time()
    return timeWork

def index(request): #функция которая принимает в качестве аргумента request (всё, что мы получим от пользователя в качестве запроса через Интернет)
    array = SortedArray.objects.all() #с помощью QuerySet(список объектов заданной модели, который позволяет читать данные из бд) отображаем на странице все масиивы
    return render(request, 'massiv/index.html', {'array': array}) # отображает переменные {'array': array} в шаблоне 'massiv/index.html'

def sort_array(request):
    if request.method == 'POST':
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            if 'action' in request.POST:
                array_name = form.cleaned_data['array_name']
                sorted_array = form.cleaned_data['sorted_array']
                numlist = sorted_array.split()
                intlist = [int(num) for num in numlist]
                intlist = selectionSort(intlist)
                #  numlist = intlist
                #  sorted_array = [str(num) for num in numlist]
                list = ''
                for a in intlist:
                    list += str(a) + ' '
                list = list[:-1]
                feed = SortedArray(
                    array_name=array_name,
                    sorted_array=list,
                )
                # Логика сохранения данных
                print(array_name)
                print(sorted_array)
                print(feed)

            feed.save()
            complex = {'form': form, 'sorted_array': sorted_array, 'array_name': array_name}

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

