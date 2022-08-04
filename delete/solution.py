def fib(numb):
    n2 = 0
    n1 = 1
    n = 0
    i = 2
    while i <= numb:
        n = n2 + n1
        n2 = n1
        n1 = n
        i += 1
    if numb == 0:
        return n2
    if numb == 1:
        return n1
    return n
