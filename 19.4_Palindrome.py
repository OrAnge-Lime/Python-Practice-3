def palindrome(s):
    #s = input()
    n = s.split(" ")
    s = "".join(n)

    s = s.lower()
    s1 = s[::-1]
    if s == s1:
        return 'Палиндром'
    else:
        return 'Не палиндром'


print(palindrome('А роза упала на лапу Азора'))