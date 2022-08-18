s = [int(input())]
while sum(s) != 0:
    s.append(int(input()))
print(sum([e * e for e in s]))
