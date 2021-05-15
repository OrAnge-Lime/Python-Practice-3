import math


def funk(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def res(t):
    return math.hypot(0.75 - t[0], 0 - t[1])


c = [(math.cos(3 * t), math.sin(3 * t)) for t in funk(0, 2 * 3.14, 0.1)]

d = [round(res(x), 4) for x in c]

print(min(d))