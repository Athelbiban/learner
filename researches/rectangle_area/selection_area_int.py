d = 43
for x in range(1, d):
    for y in range(1, d):
        if x * y == 12:
            for z in range(1, d):
                if z * y == 24:
                    for n in range(1, z + 1):
                        for q in range(1, n + 1):
                            if n > q and n + q == z:
                                for s in range(1, d):
                                    if s * q == 9 and x * s == 18:
                                        for a in range(1, d):
                                            if (s + a) * n == 42:
                                                for b in range(q, q+x + 1):
                                                    if b - q == x:
                                                        print(a, b, (a * b))
