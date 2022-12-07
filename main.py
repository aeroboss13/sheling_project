import random
import matplotlib.pyplot as plt
import numpy as np


# Получает список индексов заданного значения из двумерного массива
#Работа выполнена студентами группы БСМО-02-22 Бардиным, Болдышевым, Верховых, Макаровым
def get_indexes(element, array):
    indexes = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == element:
                indexes.append([i, j])
    return indexes


# Проверяет, счастлива ли точка
def is_happy(array, i, j, CNT_HAPPY):
    # Количество соседей того же цвета
    cnt_neigh = 0
    # Перебор всех соседей
    for shift_i in range(3):
        for shift_j in range(3):
            # Координаты соседей
            neigh_i = shift_i + i - 1
            neigh_j = shift_j + j - 1
            # Если координаты соседа не выходят за пределы поля И не являются той же клеткой - проверить его цвет
            if neigh_i >= 0 and neigh_j >= 0 and neigh_i < len(array) and neigh_j < len(array) and not (
                    i == neigh_i and j == neigh_j):
                # Если цвет одинаковый - увеличить количество соседей
                if array[i][j] == array[neigh_i][neigh_j]:
                    cnt_neigh += 1
            else:
                # Если это не сосед - не проверять
                continue
    # Если количество соседей больше или равно достаточному количеству -> вернуть true
    if cnt_neigh >= CNT_HAPPY:
        return True
    else:
        return False


def print_array(array):
    plt.rcParams["figure.figsize"] = (5, 5)
    data = np.array(field)

    x = np.arange(len(array))
    y = np.arange(len(array))

    x, y = np.meshgrid(x, y)

    plt.scatter(x, y, c=data[x, y], marker='s', s=400)
    plt.show()


# Размерность массива
N = 15

# Процентные соотношения цветов
PRC_BLUE, PRC_RED = 45, 45

# Сколько клеток рядом нужно для счастья
CNT_HAPPY = 2

# Максимальное количество шагов
STEPS = 10000

# Сколько клеток нужно заполнить цветами
count_blue = round((N * N) * PRC_BLUE / 100)
count_red = round((N * N) * PRC_RED / 100)
count_none = N * N - (count_blue + count_blue)

# Одномерный массив (словарь) для перемешивания
dictionary = []

# Заполнение словаря
for i in range(count_blue):
    dictionary.append('blue')
for i in range(count_red):
    dictionary.append('red')
for i in range(count_none):
    dictionary.append('none')

# Рандомизация элементов в словаре
random.shuffle(dictionary)


# Двумерный массив (поле эксперимента)
field = [['none' for i in range(N)] for i in range(N)]

# Заполнение массива из рандомизированного словаря
for i in range(N):
    row_start = i * N
    row_end = (i + 1) * N
    field[i] = dictionary[row_start:row_end]

# Вывод массива
print(field)

# Преобразование в массив цифр
for i in range(N):
    for j in range(N):
        if field[i][j] == 'red':
            field[i][j] = 1
        elif field[i][j] == 'blue':
            field[i][j] = 2
        else:
            field[i][j] = 0

# Количество счастливых на старте
cnt_happy_start = 0
for i in range(N):
    for j in range(N):
        # Если точка не счастлива
        if is_happy(field, i, j, CNT_HAPPY):
            cnt_happy_start += 1
print('Количество счастливых точек при старте: ', cnt_happy_start)
print_array(field)

# Фактическое количество шагов
steps_fact = 0

# Модель Шеллинга
for step in range(STEPS):
    for i in range(N):
        for j in range(N):
            # Если точка не счастлива
            if not is_happy(field, i, j, CNT_HAPPY):
                # Найти ей случайное место из пустых
                new_place = random.choice(get_indexes(0, field))
                new_place_i = new_place[0]
                new_place_j = new_place[1]
                # Поместить несчастную точку в случайное пустое место
                field[new_place_i][new_place_j], field[i][j] = field[i][j], field[new_place_i][new_place_j]
    steps_fact += 1

# Количество счастливых в конце
cnt_happy_end = 0
for i in range(N):
    for j in range(N):
        # Если точка не счастлива
        if is_happy(field, i, j, CNT_HAPPY):
            cnt_happy_end += 1
print('Количество счастливых точек в конце: ', cnt_happy_end)

print('Количество шагов: ', steps_fact)
print(field)

print_array(field)