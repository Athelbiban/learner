s = [int(i) for i in input().split()]
print(sum([s[i] > s[i-1] for i in range(1, len(s))]))
