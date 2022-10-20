from envparse import env
from win_lose import count
import os
import random

env.read_envfile('setting.env')
my_money = int(os.environ.get('MY_MONEY'))


def game(mymoney):
    slot_list = list(range(1,31))
    print('отгадайте число от 1 до 30')
    print(f'начальные деньги - {mymoney}')
    rnd_num = random.choice(slot_list)
    try:
        bet = int(input('Bаша ставка: '))
        x = int(input('Какое число загадано? '))
    except:
        print('Напишите число')
    
    mymoney = count(x, rnd_num, mymoney, bet)
    print(mymoney)

    if mymoney <= 0 :
        print('у вас закончились деньги')
        return 0

    print('Продолжить играть? ()')
    response = ''
    while response != 'N':
        response = input("Нажмите N, если отказываетесь:")
        break

    if response.upper() == 'N':
        print(f'Вы ушли с {mymoney}')
        return 0
    else:
        print(f'Вы решили продолжить c {mymoney}')
        game(mymoney)


def launch():
    while True:
        t = game(my_money)
        if t == 0:
            break
    return print('Вы перестали играть')