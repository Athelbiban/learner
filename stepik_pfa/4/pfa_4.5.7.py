x = [[e for e in input().split()] for _ in range(int(input()))]
x.reverse()

for i in map(list, zip(*x)):
    print(*i)
