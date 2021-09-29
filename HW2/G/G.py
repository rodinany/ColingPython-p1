def solution(a, b):
    c = []
    d, e = tuple(a[:]), tuple(b[:])
    while a and b:
        if a[0] != b[0]:
            if min(a[0],b[0]) == b[0]:
                if b[0] not in d:
                    c.append(b[0])
                    del b[0]
                else:
                    del b[0]
            else:
                c.append(a[0])
                del a[0]
        else:
            c.append(a[0])
            del a[0]
            del b[0]
    x = max(a,b)
    for i in x:
        if x == b:
            if i in e and i not in d:
                c.append(i)
        else:
            c.append(i)
    return c
