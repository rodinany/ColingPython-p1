def solution(n,k):
    soldiers = list(range(1, n+1))
    l = 0
    while len(soldiers) != 1:
        for x in range(len(soldiers)):
            l += 1
            if l == k:
                del soldiers[x]
                soldiers = soldiers[x:] + soldiers[:x]
                l = 0
                break
    return soldiers[0]
