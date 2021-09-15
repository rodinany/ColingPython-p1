def solution(a):
    m = len(a)
    n = len(a[0])
    b = []
    for i in range(n):
        b.append([])
        for j in range(m):
            b[i].append(a[j][i])
    return b
