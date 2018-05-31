for i in range(999, 10000):
    send = str(i)
    if len(send) == 4:
        s = send[0]
        e = send[1]
        n = send[2]
        d = send[3]
    elif len(send) == 3:
        s = str(0)
        e = send[0]
        n = send[1]
        d = send[2]
    elif len(send) == 2:
        s = str(0)
        e = str(0)
        n = send[0]
        d = send[1]
    else:
        s = str(0)
        e = str(0)
        n = str(0)
        d = send[0]
    for j in range(999, 100000):
        more = str(j)
        if len(more) == 4:
            m = more[0]
            o = more[1]
            r = more[2]
            e1 = more[3]
        elif len(more) == 3:
            m = str(0)
            o = more[0]
            r = more[1]
            e1 = more[2]
        elif len(more) == 2:
            m = str(0)
            o = str(0)
            r = more[0]
            e1 = more[1]
        else:
            m = str(0)
            o = str(0)
            r = str(0)
            e1 = more[0]
        for y in range(0,10):
            if e1 == e:
                money = int(m+o+n+e+str(y))
                if int(s+e+n+d) + int(m+o+r+e) == money:
                    print(money)
