def gem(l):
    n = []
    while l.__len__() != 0:
        max_num = ord('z')
        word = ''
        for i in l:
            if ord(i[0].lower()) < max_num:
                max_num = ord(i[0].lower())
                word = i
            elif ord(i[0].lower()) == max_num:
                j = 1
                while word[j] == i[j]:
                    j += 1

                if ord(i[j].lower()) < ord(word[j].lower()):
                    word = i
        n.append(word)
        l.remove(word)

    return n


print(gem(['mother', 'Daddy', 'sIster']))
