n = "еЕаАоОэЭуУяЯиИюЮ"


def num_of_syllable(s):
    res = 0
    for i in range(s.__len__()):
        if n.__contains__(s[i]):
            res += 1
    return res


def funk(s):
    syll_in_str = [num_of_syllable(x) for x in s.split(" ")]

    if s != "":
        res = [x for x in syll_in_str if x == syll_in_str[0]]

    if res.__len__() == syll_in_str.__len__():
        print('Парам пам-пам')
    else:
        print("Пам парам")


funk('пара-ра-рам рам-пам-папам па-ра-па-дам')
