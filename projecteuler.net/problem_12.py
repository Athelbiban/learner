import time

start = time.time()


def foo(num):
    lst = list(range(num + 1))
    for i in range(2, int(num ** 0.5) + 1):
        if lst[i]:
            for y in range(i * i, num + 1, i):
                lst[y] = 0
    lst = sorted(list(set(lst)))[2:]
    return moo(num, lst)


def moo(x, d):
    s = []
    if x == 1:
        return s
    for i in d:
        def boo(a, b):
            if a % b == 0:
                c = a // b
                s.append(b)
                return boo(c, b)
            return
        boo(x, i)
    return s


def voo(num):
    stp = foo(num)
    z = 1
    for i in set(stp):
        z *= stp.count(i) + 1
    return z


n = 1
while True:
    k = int(n/2*(n+1))
    d = voo(k)
    # for i in range(1, n + 1):
    #     k += i
    # for e in range(2, k // 2 + 1):
    #     if not k % e:
    #         d += 1
    if d < 150:
        n += 1
    else:
        break

print(k, d, n)
end = time.time() - start
print(end)
