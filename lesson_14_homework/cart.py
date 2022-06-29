import random


class Card:

    def __init__(self):
        name = (input('Введите имя игрока: '))
        name = name if name else 'Computer'
        self.name = ' ' + name + ' '
        self.numbers = []
        self.indexes = []
        self.card = [list(' ' * 20), list(' ' * 20), list(' ' * 20)]
        self.__number_generator()
        self.__card_form_generator()
        self.numbers = sorted(self.numbers)
        self.check_win = False

    # def test

    def __number_generator(self):
        numbers = set()
        while len(numbers) < 15:
            number = random.randint(1, 90)
            numbers.add(number)
        numbers = list(numbers)
        for i in range(3):
            self.numbers.append(sorted(list(numbers[i*5:(i+1)*5])))

    def __string_generator(self):
        indexes = set()
        while len(indexes) < 5:
            number = random.randint(0, 19)
            indexes.add(number)
        self.indexes.append(list(indexes))

    def __card_form_generator(self):
        for i in range(3):
            self.__string_generator()

    def cross_numeral(self, numeral):
        for i in range(3):
            if numeral in self.numbers[i]:
                index = self.numbers[i].index(numeral)
                self.numbers[i][index] = 'x'
                self.card_generator()
                answer = f'Отлично! Номер {numeral} есть у игрока{self.name}'
                break
            else:
                answer = f'Такого номера нет в карточке игрока{self.name}'
        print(answer)

    def card_generator(self):
        for i in range(3):
            self.card[i] = list(' ' * 20)
            for j in range(5):
                self.card[i][self.indexes[i][j]] = self.numbers[i][j]
        for i in range(3):
            my_str = ''
            for el in self.card[i]:
                my_str += str(el) + ' '
                self.card[i] = my_str

        max_len = max(len(self.card[0].rstrip()),
                      len(self.card[1].rstrip()),
                      len(self.card[2].rstrip()))
        if (max_len - len(self.name)) % 2 == 0:
            left_decor = int((max_len - len(self.name)) / 2)
            right_decor = int((max_len - len(self.name)) / 2)
        else:
            left_decor = int((max_len - len(self.name) - 1) / 2)
            right_decor = int((max_len - len(self.name) + 1) / 2)

        print('-' * (left_decor-1), self.name, '-' * (right_decor-1))
        print(self.card[0])
        print(self.card[1])
        print(self.card[2])
        print('-' * max_len)


if __name__ == '__main__':
    card = Card()
    card.card_generator()
    card.cross_numeral(25)
    card.cross_numeral(26)
    card.cross_numeral(27)
    card.cross_numeral(28)
    card.cross_numeral(21)
    card.cross_numeral(22)
    card.cross_numeral(23)
    card.cross_numeral(24)
