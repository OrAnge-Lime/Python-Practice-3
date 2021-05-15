import sys


l = list(map(str.strip, sys.stdin))
l1 = [s.strip() for s in l]
output = list(filter(lambda word: word[0] == '#', l1))
for i in range(l1.__len__()):
    print(str(i+1) + ' Line: ' + l1[i][1:].strip())
