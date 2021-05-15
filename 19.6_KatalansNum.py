def catalan(num):
    if num == 0:
        return 1
    else:
        c = 0
        for i in range(num):
            c += catalan(i)*catalan(num-i-1)
        return c


print(catalan(3))