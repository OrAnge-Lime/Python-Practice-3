first = input()
matrix = list(map(lambda x : int(x), first.split(' ')))
for i in range(first.split(' ').__len__()-1):
    matrix += list(map(lambda x : int(x), input().split(' ')))

print(not all(matrix))
