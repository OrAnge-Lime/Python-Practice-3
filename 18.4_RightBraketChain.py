def bracket_check(test_string):
    k = 0
    for i in range(test_string.__len__()):
        if test_string[i] == "(":
            k += 1
        elif test_string[i] == ")":
            k -= 1

        if k < 0:
            break

    if k == 0:
        print("YES")
    else:
        print("NO")


bracket_check(input())
