def solution(arr):
    new_arr = []
    while arr:
        new_arr += arr.pop(0)
        arr = list(zip(*arr))
        arr.reverse()
    return new_arr
