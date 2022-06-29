# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
# Это могут быть функции консольного файлового менеджера,
#а так же программы мой счет и программы викторина

import os
import use_functions
import file_manager
import borndayforewer


def test_view_sys_info():
    assert file_manager.view_sys_info() == 'win32'


def test_view_file():
    assert file_manager.view_file() == ['.idea', '.pytest_cache', 'borndayforewer.py', 'file_manager.py', 'pyvenv.cfg', 'test_filemanager.py', 'test_python.py', 'use_functions.py']


def test_view_dir():
    assert file_manager.view_dir() == ['Include', 'Lib', 'Scripts', '__pycache__']
#
#
# def view_sys_info():