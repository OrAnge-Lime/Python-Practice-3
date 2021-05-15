def golden_ratio(i):
    res = 1
    prev = 1
    for j in range(i-1):
        t = prev
        prev = res
        res += t
    print(res/prev)


golden_ratio(4)