import random


class Bag:

    total = 0
    keg_list = []

    def __init__(self):
        # self.total = 90
        self.keg_list = list(i for i in range(1, 91))

    def get_keg(self):
        number = 0
        while number not in self.keg_list:
            number = random.randint(1, 91)
        self.keg_list.remove(number)
        return number


if __name__ == '__main__':
    bag = Bag()
    bag.get_keg()
