#pragma once
// Подключение необходимых библиотек и объявление функций
#include <vector>
#include <iostream>
#include <ctime>
#include <fstream>

enum { yes = 1, no = 2 };
using namespace std;

vector<int> selectionSort(vector<int> array);
int isNumber();
int isNumber(int i, int j);
void saveArray(vector<int> array, vector<int> sortedArray);

