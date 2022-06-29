import random
import cart
import bag
import decors

def game_round(player_number):
    print(f'Проверяем, есть ли номер {keg_number} '
          f'у игрока{player_list[player_number].name}')
    player_list[player_number].cross_numeral(keg_number)
    check_win_list.append(player_list[player_number].numbers[0].count('x') +
                          player_list[player_number].numbers[1].count('x') +
                          player_list[player_number].numbers[2].count('x'))

print('Старт игры')
bag = bag.Bag()
player_list = []
check_win_list = []
check_loose_list = []
players_number = int(input('Введите колличество игроков: '))

for i in range(players_number):
    player = cart.Card()
    player_list.append(player)
    check_win_list.append(player.numbers[0].count('x') +
                          player.numbers[1].count('x') +
                          player.numbers[2].count('x'))
    player.card_generator()
while check_win_list.count(15) < 1:
    for i in range(players_number):
        check_win_list.clear()
    print('Следующий раунд')
    print(f'В мешке осталось {len(bag.keg_list)} боченков')
    keg_number = bag.get_keg()
    for i in range(players_number):
        if player_list[i].name == ' Computer ':
            game_round(i)
        else:
            if player_list[i].name not in check_loose_list:
                player_answer = input(f'{player_list[i].name}, желаете зачеркнуть цифру? y/n: ')
                if player_answer == 'y':
                    if (keg_number not in player_list[i].numbers[0]) and (keg_number not in player_list[i].numbers[1]) and (keg_number not in player_list[i].numbers[2]):
                        print(f'Сорян, {player_list[i].name}, вы проиграли.')
                        check_loose_list.append(player_list[i].name)
                    else:
                        game_round(i)
                else:
                    if (keg_number in player_list[i].numbers[0]) or (
                            keg_number in player_list[i].numbers[1]) or (
                            keg_number in player_list[i].numbers[2]):
                        print(f'Сорян, {player_list[i].name}, вы проиграли.')
                        check_loose_list.append(player_list[i].name)

                    else:
                        game_round(i)


for i in range(players_number):
    if player_list[i].name in check_loose_list:
        player_list[i] = ' '

for i in range(players_number):
    if ' ' in player_list:
        player_list.remove(' ')
print(f'Игра окончена. Победитель - '
      f'{player_list[check_win_list.index(15)].name}')

