
from massiv.models import SortedArray
from massiv.views import selectionSort
from django.shortcuts import render
from django.shortcuts import redirect
from random import randint

import time

import sqlite3
# Create your tests here.


def test(request):

    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from massiv_sortedarray"""
    cursor.execute(sqlite_select_query)

    done = True
    count = 1
    limit = 100
    doing = 1
    timeWork = ""

    for k in range(1, 1 + doing):
        start = time.time()
        for i in range(1, count + 1):  # Цикл по количеству массивов
            size = randint(2, limit)
            list = ''
            for j in range(0, size):  # Цикл по одному массиву
                # feel.sorted_array.append(randint(0,limit))
                list += str(randint(0, limit)) + ' '
            list = list[:-1]
            sorted_array = list
            feel = SortedArray(
                array_name=str(k) + "." + str(i),
                sorted_array=list,
            )
            if (feel.save() == False):
                done = False
        end = time.time()
        if (done == True):
            timeWork += "Массив на " + str(count) + " символов выполнен успешно. Время работы : " + str(round((end-start),2))+" с.   "
        else:
            timeWork += "Массив на " + str(count) + " символов выполнен неуспешно."
        if (k != 1 + doing):
            count *= 10

    complex = {'count': count, 'i': i, 'Success': done, 'timeWork': timeWork}
    testDownload()
    return render(request, 'massiv/test.html', complex)


def testDownload():
    pr = ""
    pri = ""
    startFunc = time.time()
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from massiv_sortedarray"""
    cursor.execute(sqlite_select_query)
    size=100
    for k in range(0,3):
        startSize = time.time()
        for i in range(0,size):
            records=cursor.fetchmany(size)
            for j in range(0,len(records)):
                sortArray=records[j][2]
                numlist = [int(x) for x in sortArray.split()]
                arr,success=selectionSort(numlist)
        endSize=time.time()
        roundsize=4
        timeWorkSize=round((endSize-startSize),roundsize)
        if(success):
            pr += "Выгрузка и сортировка "+str(size)+" массивов выполнены за "+ str(round(timeWorkSize,roundsize)) +" с." + " Среднее время работы с одним массивом: "+str(round(timeWorkSize/size,roundsize))+ " с."
        else:
            pr += "При выгрузке или сортировке произошла ошибка"
        size *= 10
    endFunc=time.time()
    timeAll=round((endFunc-startFunc),roundsize)
    pri += "Время работы всей функции: "+str(timeAll)+" с. "
    cursor.close()

    complex = {'pr': pr, 'pri': pri}
    return redirect('massiv/test.html', complex)