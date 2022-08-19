s, r = input(), ''

if len(s) > 3:
    for _ in range(len(s) // 3):
        r = ',' + s[-3:] + r
        s = s[:-3]

print(s + r if s else r[1:])
