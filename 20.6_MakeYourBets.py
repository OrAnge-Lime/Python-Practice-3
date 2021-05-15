bets = []


def do_bet(a, b):
    if bets.__contains__(a):
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        if a > 10 or b == 0:
            print("Что-то пошло не так, попробуйте еще раз")
        else:
            bets.append(a)
            print('Ваша ставка в размере ' + str(b) + ' на лошадь ' + str(a) + ' принята')


do_bet(1, 10)
do_bet(1, 100)
do_bet(2, 0)
do_bet(2, 200)
