def solution(arr):
    amount = []
    n = 1
    if arr:
        amount.append(n)

    for x in range(0, len(arr)-1):
        if arr[x] == arr[x+1]:
            n += 1
        else:
            amount.append(n)
            n = 1
    return max(amount)
