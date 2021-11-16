def integers():
    i = 1
    while True:
        yield i
        i += 1

def take(n, generator):
    k = 0
    a = []
    m = generator
    while k < n:
        a.append(next(m))
        k += 1
    return a

def squares():
    m = integers()
    while True:
        yield next(m)**2

print(take(5, squares()))