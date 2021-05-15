from math import sqrt


def solve(*coefficients):
    if coefficients.__len__() == 0 or coefficients.__len__() > 3:
        return None
    elif coefficients.__len__() == 2:
        return coefficients[1] / coefficients[0]
    elif coefficients.__len__() == 3:
        res = []
        d = coefficients[1] * coefficients[1] - 4 * coefficients[0] * coefficients[2]
        if d > 0:
            res.append((-coefficients[1] + sqrt(d)) / 2 * coefficients[0])
            res.append((-coefficients[1] - sqrt(d)) / 2 * coefficients[0])
        elif d == 0:
            res.append((-coefficients[1] + sqrt(d)) / 2 * coefficients[0])
        return res


print(sorted(solve(1, -3, 2)))
