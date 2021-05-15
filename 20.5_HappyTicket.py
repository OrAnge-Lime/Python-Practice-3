lastTicket = 123321

def lucky(ticket):
    t = str(ticket)
    if t.__len__()<6:
        while t.__len__() < 6:
            t += '0'

    lt = str(lastTicket)
    if int(t[0]) + int(t[1]) + int(t[2]) == int(t[3]) + int(t[4]) + int(t[5]) and int(lt[0]) + int(lt[1]) + int(lt[2])\
            == int(lt[3]) + int(lt[4]) + int(lt[5]):
        return "Счастливый"
    else:
        return "Несчастливый"


print(lucky(100001))