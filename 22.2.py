def partial_sums(*s):
    res = [0]
    sum = 0
    for i in s:
        sum += i
        res.append(sum)

    return res


print(partial_sums(1, 0.5, 0.25, 0.125))
