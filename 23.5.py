def same_by(characteristic, objects):
    c = list(map(characteristic, objects))
    if len(c) > 0:
        s = [x for x in c if x == c[0]]
        if s.__len__() == c.__len__():
            return True
        else:
            return False
    else:
        return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
