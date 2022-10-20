def count(x, rnd_num, mymoney, bet):
    if x == rnd_num:
        mymoney += bet * 2
        return mymoney
    else:
        mymoney -= bet
        return mymoney
