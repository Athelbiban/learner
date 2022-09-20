d = {}

for _ in range(int(input())):
    v, *k = input().split()
    d[tuple(k)] = v

for _ in range(int(input())):
    t = input()
    for i in d:
        if t in i:
            print(d[i])
            break

# [print(d[i]) for _ in range(int(input())) for t in [input()] for i in d if t in i] # То же самое но одной строкой
