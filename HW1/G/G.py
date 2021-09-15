def solution(a, b):
    c = []
    for x in b:
        if x not in a:
            c.append(x)
    c = a + c
    c.sort()
    return c

