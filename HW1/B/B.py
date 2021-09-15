def solution(n):
    a = ('   _~_   ' * n + '\n' + '  (o o)  ' * n  + '\n' +
              ' /  V  \ ' * n + '\n' + '/(  _  )\\' * n
               + '\n' + '  ^^ ^^  ' * n)
    if not a.strip():
        a = ''
        
    return a
