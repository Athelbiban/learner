a = ''

for i in input():
    if i == a[-1]:
        a += i
    else:
        a += ' ' + i

s = ''

for i in a.split():
    if len(i) > 1:
        s += str(len(i)) + i[0]
    else:
        s += i[0]
print(s)
