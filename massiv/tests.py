
from massiv.models import SortedArray

from django.shortcuts import render

from random import randint

import time

import sqlite3
# Create your tests here.






def test(request):
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    cursor.execute("""DELETE FROM  massiv_sortedarray""")
    sqlite_connection.commit()
    done=True
    count = 100
    limit = 100
    doing = 3
    timeWork=""
    for k in range(1,1+doing):
        start=time.time()
        for i in range(1, count+1): # Цикл по количеству массивов
            size = randint(2, limit)
            feel = SortedArray(
                array_name=str(k)+"."+str(i),
                sorted_array=[],
            )
            for j in range(0,size): # Цикл по одному массиву
                feel.sorted_array.append(randint(0,limit))
            if(feel.save()==False):
                done=False

        end=time.time()
        if(done==True):
            timeWork+="Массив на " +str(count)+ " символов выполнен успешно. Время работы : "+str(round((end-start),2))+" с.   "
        else:
            timeWork += "Массив на " + str(count) + " символов выполнен неуспешно."
        if (k != 1 + doing):
            count *= 10

    complex = {'count': count, 'i': i,'Success': done, 'timeWork': timeWork}

    return render(request,'massiv/test.html', complex)

