def equation(x, y):
    x1 = float(x.split(";")[0])
    y1 = float(x.split(";")[1])

    x2 = float(y.split(";")[0])
    y2 = float(y.split(";")[1])

    if x1 == x2:
        print(x1)
    elif y1 == y2:
        print(y1)
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        print(k, b)



