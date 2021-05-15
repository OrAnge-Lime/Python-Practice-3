a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def encrypt_caesar(msq, shift):
    res = ''
    for i in range(msq.__len__()):
        if msq[i].isupper():
            a1 = a.upper()
        else:
            a1 = a

        if a1.__contains__(msq[i]):
            res += a1[(a1.index(msq[i])+shift) % a1.__len__()]
        else:
            res += msq[i]
        a1.lower()
    return res


def decrypt_caesar(msq, shift):
    res = ''
    for i in range(msq.__len__()):
        if msq[i].isupper():
            a1 = a.upper()
        else:
            a1 = a

        if a1.__contains__(msq[i]):
            res += a1[(a1.index(msq[i]) - shift) % a1.__len__()]
        else:
            res += msq[i]
        a1.lower()
    return res


msg = 'Да здравствует салат Цезарь!'
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
