def solution(x):
    l = len(x)
    if 'h' in x:
        h_amount = x.count('h')
        n = 0
        for i in range(l):
            if x[i] == 'h':
                n += 1
                if n > 1 and n < h_amount:
                    x = x[:i] + 'H' + x[i+1:]
                    l = len(x)
                else:
                    continue
    m = ''
    for i in range(len(x)):
        if i == 0 or i % 3 != 0:
            m = m + x[i]
    x = m
    l = len(x)
    while True:
        if '1' in x:
            for i in range(l):
                if x[i] == '1':
                    x = x[:i] + 'one' + x[i+1:]
                    l = len(x)
        else:
            break
    return x
