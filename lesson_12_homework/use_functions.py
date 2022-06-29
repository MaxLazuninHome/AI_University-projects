"""
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""
import json
import os

class Balance:

    balance = ''
    history = {'Название покупки': 'Стоимость'}

    def __init__(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        try:
            with open('balance.txt', 'r') as f:
                self.balance = int(f.read())
        except(FileNotFoundError):
            print('Создадим счёт')
            with open('balance.txt', 'w') as f:
                f.write('0')
            with open('balance.txt', 'r') as f:
                self.balance = int(f.read())
        try:
            with open('history.json', 'rb') as f:
                self.history = json.load(f)
        except(FileNotFoundError):
            print('Создадим историю расходов')
            with open('history.json', 'w') as f:
                json.dump(self.history, f)
                self.history = json.load(f)
        print(f'Поздравляем, Ваш счёт составляет {self.balance} рублей!')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def increase(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        sum_in = int(input('Какую сумму желаете внести? '))
        self.balance += sum_in
        print(f'Прекрасно! Теперь Ваш счёт составляет {self.balance} рублей')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def decrease(self):
        print('-' * 10 + '  Начало операции  ' + '-' * 10)
        sum_out = int(input('Какую сумму желаете потратить? '))
        if sum_out <= self.balance:
            self.balance -= sum_out
            purchase = input('Введите название вашей покупки: ')
            self.history.update([(purchase, str(sum_out) + ' руб')])
        else:
            print('Извините, на счёте недостаточно средств.')
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()

    def my_history(self):
        obj_list = self.history.items()
        for item in obj_list:
            print(item)
        print('-' * 10 + '  Конец операции  ' + '-' * 10)
        print()


def create_account():
    my_balance = Balance()
    while True:
        print('0. Пересоздание счёта')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '0':
            remake = input('Вы уверены, что хотите пересоздать счёт? y/n: ')
            if remake == 'y':
                with open('balance.txt', 'w') as f:
                    f.write('0')
                with open('history.json', 'w') as f:
                    json.dump({'Название покупки': 'Стоимость'}, f)
                my_balance = Balance()
            else:
                continue
        if choice == '1':
            my_balance.increase()
        elif choice == '2':
            my_balance.decrease()
        elif choice == '3':
            my_balance.my_history()
        elif choice == '4':
            print('Спасибо за обращение! Хорошего дня!')
            with open('balance.txt', 'w') as f:
                f.write(str(my_balance.balance))
            with open('history.json', 'w') as f:
                json.dump(my_balance.history, f)
            break
        else:
            print('Неверный пункт меню')


create_account()