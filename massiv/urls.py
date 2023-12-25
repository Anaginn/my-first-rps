"""Как ты можешь заметить, мы связали view под именем post_list с корневым URL-адресом (''). Этот шаблон URL будет
соответствовать пустой строке. Это правильно, потому что для обработчиков URL в Django 'http://127.0.0.1:8000/'
не является частью URL. Этот шаблон скажет Django, что views.post_list — это правильное направление для запроса к
твоему веб-сайту по адресу 'http://127.0.0.1:8000/'.

Последняя часть name='post_list' — это имя URL, которое будет использовано, чтобы идентифицировать его. Оно может быть
таким же, как имя представления (англ. view), а может и чем-то совершенно другим. Мы будем использовать именованные URL
позднее в проекте, поэтому важно указывать их имена уже сейчас. Мы также должны попытаться сохранить имена URL-адресов
уникальными и легко запоминающимися.

Фрагмент post/<int:pk>/ определяет шаблон URL-адреса. Сейчас мы его поясним:

post/ значит, что после начала строки URL должен содержать слово post и косую черту /. Пока всё в порядке.
<int:pk> — эта часть посложнее. Она означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.
/ — затем нам нужен еще один символ / перед тем, как адрес закончится."""


from django.urls import path
from massiv import views
from massiv import tests
from massiv import sorting

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('selection_sort', sorting.selection_sort, name='selection_sort'),
    path('test', tests.test, name='test'),
    path('test_clear', tests.test_clear, name='test_clear'),
    path('test_output', tests.test_output, name='test_output'),
    path('test_download', tests.test_download, name='test_download'),
]