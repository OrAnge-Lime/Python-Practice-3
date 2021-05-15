i = int(input())
l = []
for i in range(i):
    a = input().lower()
    if not l.__contains__(a):
        l.append(a)

res = []

while l.__len__() != 0:
    s = l[0]
    word = l[0]
    l.remove(l[0])

    for i in l:
        t = True
        for j in i:
            if not word.__contains__(j):
                t = False
                break

        if t:
            for j in word:
                if not i.__contains__(j):
                    t = False
                    break

        if t:
            s += ' ' + i
            l.remove(i)

    res.append(s)

print(res)
