s, t, n = input(), input(), 0

while t in s:
    s = s[s.find(t)+1:]
    n += 1
print(n)
