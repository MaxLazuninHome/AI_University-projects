'''
(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
'''

# Вариант со списками и циклами

first_list = input('Введите первый набор чисел: ')
second_list = input('Введите второй набор чисел: ')
first_list = first_list.replace('/', ' ').replace(';', ' ').replace(',', ' ').split()
second_list = second_list.replace('/', ' ').replace(';', ' ').replace(',', ' ').split()
for i in range(len(first_list)):
    first_list[i] = int(first_list[i])
for i in range(len(second_list)):
    second_list[i] = int(second_list[i])
new_list = []
for el in first_list:
    if el in second_list:
        continue
    else:
        new_list.append(el)
print(new_list)

# Вариант со множествами

first_list = input('Введите первый набор чисел: ')
second_list = input('Введите второй набор чисел: ')
for i in range(len(first_list)):
    first_list[i] = int(first_list[i])
for i in range(len(second_list)):
    second_list[i] = int(second_list[i])

new_list = []
first_list = first_list.replace('/', ' ').replace(';', ' ').replace(',', ' ').split()
second_list = second_list.replace('/', ' ').replace(';', ' ').replace(',', ' ').split()
first_set = set(first_list)
second_set = set(second_list)
print(list(first_set - second_set))
