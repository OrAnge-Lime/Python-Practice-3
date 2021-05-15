from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    res = []
    if a == 0:
        if b == 0:
            if c == 0:
                res.append("all")
        else:
            res.append(-c/b)
    else:
        d = b*b - 4*a*c
        if d > 0:
            res.append((-b + sqrt(d))/2*a)
            res.append((-b - sqrt(d))/2*a)
        elif d == 0:
            res.append((-b + sqrt(d)) / 2 * a)

    return res


result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))
