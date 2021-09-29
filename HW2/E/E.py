def solution(a, b):
    if b == 0:
        return a
    else:
        return solution(a+1, b-1)
