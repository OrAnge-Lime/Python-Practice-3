def possible_turns(cell):
    res = []
    vv = "ABCDEFGH"
    h = int(cell[1])
    v = vv.index(cell[0])+1

    if h <= 6:
        if v > 1:
            s = str(vv[v])+str(h+2)
            res.append(s)
        if v < 8:
            s = str(vv[v-2])+str(h+2)
            res.append(s)

    if h <= 7:
        if v > 2:
            s = str(vv[v-1])+str(h+1)
            res.append(s)
        if v < 7:
            s = str(vv[v + 1]) + str(h + 1)
            res.append(s)

    if h >= 3:
        if v > 1:
            s = str(vv[v - 2]) + str(h - 2)
            res.append(s)
        if v < 8:
            s = str(vv[v]) + str(h - 2)
            res.append(s)

    if h >=2:
        if v > 2:
            s = str(vv[v - 3]) + str(h - 1)
            res.append(s)
        if v < 7:
            s = str(vv[v + 1]) + str(h - 1)
            res.append(s)

    res.sort()
    return res


print(possible_turns("B1"))