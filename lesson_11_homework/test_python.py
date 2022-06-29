#  B модуле написать тесты для встроенных функций filter, map, sorted,
#  а также для функций из библиотеки math: pi, sqrt, pow, hypot.
#  Чем больше тестов на каждую функцию - тем лучше

import os
import math
my_list = [1, 3, 2, 4, 6, 5]


def test_sort():
    sort_list = sorted(my_list)
    assert sort_list == [1, 2, 3, 4, 5, 6]


def test_filter():
    os.mkdir('test_folder')
    assert 'test_folder' in os.listdir(), 'Уже'
    os.rmdir('test_folder')


def test_map():
    assert list(map(lambda x: x * 2 + 3, my_list)) == [5, 9, 7, 11, 15, 13]


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(4) == 2


def test_pow():
    assert  math.pow(2, 5) == 32


def test_hupot():
    assert  math.hypot(3, 4) == 5


# test_sort()
# test_filter()
# test_map()
