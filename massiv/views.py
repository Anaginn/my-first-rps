from massiv.models import SortedArray
from django.shortcuts import render, get_object_or_404
from massiv.forms import SortedArrayForm
from django.shortcuts import redirect


def index(request): #функция которая принимает в качестве аргумента request (всё, что мы получим от пользователя в качестве запроса через Интернет)
    array = SortedArray.objects.all()[:100] #с помощью QuerySet(список объектов заданной модели, который позволяет читать данные из бд) отображаем на странице все масиивы
    return render(request, 'massiv/index.html', {'array': array}) # отображает переменные {'array': array} в шаблоне 'massiv/index.html'



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


