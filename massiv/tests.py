from massiv.models import SortedArray
from massiv.sorting import sort_array
from django.shortcuts import render
from random import randint
import re
import time
import sqlite3
# Create your tests here.



def test(request):    # Функция для кнопки "Тест добавления"
    # sqlite_connection = sqlite3.connect('db.sqlite3')
    # cursor = sqlite_connection.cursor()  # Delete from Database
    # cursor.execute("""DELETE FROM  massiv_sortedarray""")
    #  sqlite_connection.commit()
    done = True
    array_count = 100
    limit_size = 100
    test_count = 3
    timeWork = ""
    for k in range(1, 1 + test_count):  # Цикл по количеству отрабатываний теста(3)
        start = time.time()  # Начало отсчёта времени работы
        for i in range(1, array_count + 1):  # Цикл по количеству массивов
            size = randint(2, limit_size)  # Вычисление размера массива
            list = ''
            for j in range(0, size):  # Цикл по одному массиву
                # feel.sorted_array.append(randint(0,limit))
                list += str(randint(0, limit_size)) + ' '  # Добавление к массиву элементов
            list = list[:-1]
            #  sorted_array=list
            feel = SortedArray(  # Сохранение кортежа
                array_name=str(k) + "." + str(i),
                sorted_array=list,
            )
            if (feel.save() == False):  # Проверка ошибки сохранения
                done = False
        end = time.time()  # Фиксация окончания работы функции
        if (done == True):  # Выводы
            timeWork += "Массив на " + str(array_count) + " символов выполнен успешно. Время работы : " + str(
                round((end - start), 2)) + " с.   "
        else:
            timeWork += "Массив на " + str(array_count) + " символов выполнен неуспешно."
        if (k != 1 + test_count):  # Увеличение количества массивов
            array_count *= 10
    array_count //= 10
    complex = {'Success': done, 'timeWork': timeWork}  # Возвращаемые из функции данные

    return render(request, 'massiv/test.html', complex)


def test_download(request): # Функция для кнопки "Тест выгрузки и сортировки"
    worksize = 0
    pr = ""
    pri = ""
    success = True
    # Функция для кнопки "Тест выгрузки и сортировки"
    startFunc = time.time()  # Начало отсчёта
    sqlite_connection = sqlite3.connect('db.sqlite3')  # Подключение к БД
    sqlite_select_query = sqlite_connection.cursor()
    sqlite_select_query.execute("SELECT * FROM massiv_sortedarray")
    size = 100
    sizeDB = len(sqlite_select_query.fetchall())
    if sizeDB < ((size) * (1 + 10 + 100)):
        add(((size) * (1 + 10 + 100)) - sizeDB)
    for k in range(0, 3):  # Цикл по количеству тестов
        startSize = time.time()  # Время начала работы функции
        startRand = randint(0, sizeDB) % (sizeDB - size)
        print("StartRand is " + str(startRand))
        #  records = cursor.fetchall()[startRand:startRand+size]
        req = "SELECT * FROM massiv_sortedarray LIMIT " + str(size) + " OFFSET " + str(startRand)
        records = sqlite_select_query.execute(req)
        records = sqlite_select_query.fetchall()
        print("Len records is " + str(len(records)))
        for i in range(0, 1):  # Цикл по количеству массивов
            for j in range(0, len(records)):
                sortArray = records[j][2]  # Получение массива
                res = re.findall(r'\d+', sortArray)  # Перевод строки в числа
                numlist = list(map(int, res))
                arr, success = sort_array(numlist)  # Сортировка

        endSize = time.time()  # Время окончания работы функции
        roundsize = 4  # Переменная точности округления результатов
        timeWorkSize = round((endSize - startSize), roundsize)  # Время работы
        worksize += timeWorkSize
        if (success):  # Выводы
            pr += "\nВыгрузка и сортировка " + str(size) + " массивов выполнены за " + str(
                round(timeWorkSize, roundsize)) + " с. " + " Среднее время работы с одним массивом: " + str(
                round(timeWorkSize / size, roundsize)) + " с. \n"
        else:
            pr += "При выгрузке или сортировке произошла ошибка"
        size *= 10
    endFunc = time.time()
    timeAll = round((endFunc - startFunc), roundsize)

    pri += "Время работы всей функции: " + str(worksize) + " с. "

    complex = {'pr': pr, 'pri': pri}
    return render(request, 'massiv/test_download.html', complex)


def test_clear(request):        # Функция для кнопки "Тест очистки"
    success=True
    prin = ""
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')      # Подключение к БД и удаление записи
        cursor = sqlite_connection.cursor()
        cursor.execute("""DELETE FROM  massiv_sortedarray""")
        sqlite_connection.commit()
    except:
        success=False       # Здесь в return тебе надо будет добавить переменную success, а потом на странице написать
                            # успешно функция отработала или нет( в зависимости от значения переменной)

    if success==True:
        prin = "Удаление базы данных прошло успешно"
    else:
        prin = "При удалении базы данных произошла ошибка"

    complex = {'prin': prin}

    return render(request, 'massiv/test_clear.html', complex)


def test_output(request):   # Функция для кнопки "Вывод всей БД"
    array = SortedArray.objects.all()
    return render(request, 'massiv/test_output.html', {'array': array})

def add(sizeFill):
    limit_size = 100
    array_count = sizeFill
    for i in range(1, array_count + 1):  # Цикл по количеству массивов
        size = randint(2, limit_size)  # Вычисление размера массива
        list = ''
        for j in range(0, size):  # Цикл по одному массиву
            # feel.sorted_array.append(randint(0,limit))
            list += str(randint(0, limit_size)) + ' '  # Добавление к массиву элементов
        list = list[:-1]
        #  sorted_array=list
        feel = SortedArray(  # Сохранение кортежа
            array_name="1." + str(i),
            sorted_array=list,
        )
        if (feel.save() == False):  # Проверка ошибки сохранения
            done = False
        array_count *= 10