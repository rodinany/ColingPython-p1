def solution(n):
    powers = []
    k = 1    
    while True:
        powers.append(k)
        k += k
        if k > n:
            break
    return powers

