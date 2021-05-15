from random import randint
import string


def dop_condition(pas):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    big_letters = letters.upper()
    nums = '0123456789'
    res = pas

    check = [x for x in pas if letters.__contains__(x) or big_letters.__contains__(x)]
    if check.__len__() == pas.__len__():
        res = pas[:-2] + nums[randint(0, nums.__len__() - 1)]

    check = [x for x in pas if letters.__contains__(x) or nums.__contains__(x)]
    if check.__len__() == pas.__len__():
        res = pas[1:] + big_letters[randint(0, big_letters.__len__() - 1)]

    check = [x for x in pas if big_letters.__contains__(x) or nums.__contains__(x)]
    if check.__len__() == pas.__len__():
        p = randint(0, pas.__len__() - 1)
        pas += pas[:p] + letters[randint(0, letters.__len__() - 1)] + pas[p+1:]

    return res


def generate_password(len):
    s = string.ascii_letters + '0123456789'
    pas = ''
    forbidden_symb = 'lI1oO0'

    for i in range(len):
        n = randint(0, s.__len__() - 1)
        if pas == '':
            while forbidden_symb.__contains__(s[n]):
                n = randint(0, s.__len__() - 1)
        else:
            while forbidden_symb.__contains__(s[n]) or s[n] == pas[-1]:
                n = randint(0, string.ascii_letters.__len__() - 1)
        pas += s[n]

    return dop_condition(pas)


def main(n, m):
    return list(map(lambda x: generate_password(m), range(n)))


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
