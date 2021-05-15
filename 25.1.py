from random import randint
import string


def generate_password(len):
    pas = ''
    forbidden_symb = 'lI1oO0'

    for i in range(len):
        n = randint(0, string.ascii_letters.__len__()-1)
        if pas == '':
            while forbidden_symb.__contains__(string.ascii_letters[n]):
                n = randint(0, string.ascii_letters.__len__()-1)
        else:
            while forbidden_symb.__contains__(string.ascii_letters[n]) or string.ascii_letters[n] == pas[-1]:
                n = randint(0, string.ascii_letters.__len__()-1)
        pas += string.ascii_letters[n]
    return pas


def main(n, m):
    return list(map(lambda x: generate_password(m), range(n)))


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
