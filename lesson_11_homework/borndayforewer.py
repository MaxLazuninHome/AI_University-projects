"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
import random

def mode_chose():
    print('Выберите один из вариантов игры. Напишите 1 или 2: ')
    print('1 - Pushkins bio')
    print('2 - Random date')
    choice = int(input('Что вы выбираете? '))
    if choice == 1:
        year = input('Ввведите год рождения А.С.Пушкина:')
        while year != '1799':
            print("Не верно")
            year = input('Ввведите год рождения А.С.Пушкина:')

        day = input('Ввведите день рождения Пушкина? ')
        while day != '6':
            print("Не верно")
            day = input('В какой день июня родился Пушкин?')
        print('Верно')
    else:
        birth_list = [
            '01.01.2000']  # Оставим здесь тестовую дату для проверки корректности работы цикла. Вводим её на первой итерации игры
        days_numbers = ['Первое', 'Второе', 'Третье', 'Четвёртое', 'Пятое',
                        'Шестое',
                        'Седьмое', 'Восьмое', 'Девятое',
                        'Десятое']  # Дней много, ограничимся первыми 10
        month_numbers = ['января', 'февраля', 'марта', 'апреля',
                         'мая']  # Возьмём 5 месяцев
        answer_date = []  # Список дат в формате правильного ответа
        ans = 'y'  # Маркер для повтора игры
        while ans == 'y':
            for i in range(
                    5):  # Сгенерим случайные даты рождения. Модуль random уже используется,
                random_day = random.randint(1,
                                            10)  # поэтому сразу будем шенерировать 5 дат
                if random_day < 10:
                    random_day = str(0) + str(random_day)
                random_month = random.randint(1, 5)
                if random_month < 10:
                    random_month = str(0) + str(random_month)
                random_year = random.randint(1980, 2000)
                birth_date = str(random_day) + '.' + str(
                    random_month) + '.' + str(
                    random_year)
                birth_list.append(birth_date)
                answer_date.append(
                    str(days_numbers[int(random_day) - 1]) + ' ' + str(
                        month_numbers[int(random_month) - 1]) + ' ' + str(
                        random_year) + ' года')
            true_counter = 0
            false_counter = 0
            for i in range(5):
                checking_date = input('Введите дату в формате дд.мм.гггг: ')

                if checking_date in birth_list:
                    print('Ура, вы угадали рандомную дату')
                    true_counter += 1
                else:
                    print(f'Ну не, сорян... Правильный ответ {answer_date[i]}')
                    false_counter += 1
            print(
                f'Вы дали {true_counter} правильных и {false_counter} неправильных ответов')
            ans = input('Желаете сыграть ещё раз? y/n: ')
        print('Спасибо за игру, увидимся в следующий раз!')

if __name__ == '__borndayforever__':
    mode_chose()


