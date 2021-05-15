def prime(num):
    res = "Простое число"
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                res = "Составное число"
                break
        return res


print(prime(13))
