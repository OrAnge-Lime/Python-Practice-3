def line(s, t):
    k = float(s.split("x")[0])
    if t.__contains__("+"):
        b = float(s.split("+")[-1])
    else:
        b = float(s.split("-")[-1])*(-1)

    x = float(t.split(";")[0])
    y = float(t.split(";")[1])

    if y == x*k + b:
        print("True")
    else:
        print("False")

