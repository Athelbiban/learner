n = 4
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        for k in range(n, -n - 1, -1):
            if n - i + k == j and k < -1:
                a[i].append(0)
                break
            elif n - i + k == j and k == -1:
                a[i].append(1)
                break
            elif n - i + k == j and k > -1:
                a[i].append(2)
                break

        # if n - i - 1 == j:
        #     a[i].append(1)
        # if n - i - 2 == j:
        #     a[i].append(0)
        # if n - i - 3 == j:
        #     a[i].append(5)
        # if n - i - 4 == j:
        #     a[i].append(6)
        # if n - i == j:
        #     a[i].append(2)
        # if n - i + 1 == j:
        #     a[i].append(3)
        # if n - i + 2 == j:
        #     a[i].append(4)

for row in a:
    print(' '.join([str(i) for i in row]))
