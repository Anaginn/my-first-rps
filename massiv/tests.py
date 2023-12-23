
from massiv.models import SortedArray
from massiv.views import selectionSort
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
    count = 100
    limit = 100
    doing = 3
    timeWork = ""
    for k in range(1, 1 + doing):  # Цикл по количеству отрабатываний теста(3)
        start = time.time()  # Начало отсчёта времени работы
        for i in range(1, count + 1):  # Цикл по количеству массивов
            size = randint(2, limit)  # Вычисление размера массива
            list = ''
            for j in range(0, size):  # Цикл по одному массиву
                # feel.sorted_array.append(randint(0,limit))
                list += str(randint(0, limit)) + ' '  # Добавление к массиву элементов
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
            timeWork += "Массив на " + str(count) + " символов выполнен успешно. Время работы : " + str(
                round((end - start), 2)) + " с.   "
        else:
            timeWork += "Массив на " + str(count) + " символов выполнен неуспешно."
        if (k != 1 + doing):  # Увеличение количества массивов
            count *= 10
    count //= 10
    complex = {'Success': done, 'timeWork': timeWork}  # Возвращаемые из функции данные

    return render(request, 'massiv/test.html', complex)


def test_download(request): # Функция для кнопки "Тест выгрузки и сортировки"

    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        # Perform your operations on the table
        cursor.execute("SELECT * FROM massiv_sortedarray")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.OperationalError:
        print("Table does not exist")

    pr = ""
    pri = ""
    success = True
    # Функция для кнопки "Тест выгрузки и сортировки"
    startFunc = time.time()  # Начало отсчёта
    sqlite_connection = sqlite3.connect('db.sqlite3')  # Подключение к БД
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from massiv_sortedarray"""
    cursor.execute(sqlite_select_query)
    size = 100
    sizeDB = len(cursor.fetchall())
    print("SizeDB is " + str(sizeDB))
    if sizeDB < ((size) * (1 + 10 + 100)):
        add(((size) * (1 + 10 + 100)) - sizeDB)
    for k in range(0, 3):  # Цикл по количеству тестов
        startSize = time.time()  # Время начала работы функции
        startRand = randint(0, sizeDB) % (sizeDB - size)
        print("StartRand is " + str(startRand))
        #  records = cursor.fetchall()[startRand:startRand+size]
        req = "SELECT * FROM massiv_sortedarray LIMIT " + str(size) + " OFFSET " + str(startRand)
        records = cursor.execute(req)
        records = cursor.fetchall()
        print("Len records is " + str(len(records)))
        for i in range(0, 1):  # Цикл по количеству массивов
            for j in range(0, len(records)):
                sortArray = records[j][2]  # Получение массива
                res = re.findall(r'\d+', sortArray)  # Перевод строки в числа
                numlist = list(map(int, res))
                arr, success = selectionSort(numlist)  # Сортировка

        endSize = time.time()  # Время окончания работы функции
        roundsize = 3  # Переменная точности округления результатов
        timeWorkSize = round((endSize - startSize), roundsize)  # Время работы
        if (success):  # Выводы
            pr += "\nВыгрузка и сортировка " + str(size) + " массивов выполнены за " + str(
                round(timeWorkSize, roundsize)) + " с. " + " Среднее время работы с одним массивом: " + str(
                round(timeWorkSize / size, roundsize)) + " с. \n"
        else:
            pr += "При выгрузке или сортировке произошла ошибка"
        size *= 10
    endFunc = time.time()
    timeAll = round((endFunc - startFunc), roundsize)

    pri += "Время работы всей функции: " + str(timeAll) + " с. "

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
    limit = 100
    count=sizeFill
    for i in range(1, count + 1):  # Цикл по количеству массивов
        size = randint(2, limit)  # Вычисление размера массива
        list = ''
        for j in range(0, size):  # Цикл по одному массиву
            # feel.sorted_array.append(randint(0,limit))
            list += str(randint(0, limit)) + ' '  # Добавление к массиву элементов
        list = list[:-1]
        #  sorted_array=list
        feel = SortedArray(  # Сохранение кортежа
            array_name="1." + str(i),
            sorted_array=list,
        )
        if (feel.save() == False):  # Проверка ошибки сохранения
            done = False
        count *= 10