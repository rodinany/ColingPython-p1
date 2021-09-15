def solution(n, k):
    a = k // n
    b = k - a * n
    return a, b
