v, t = int(input()), int(input())
s = 109
x = v * t

if v >= 0:
    if x > s:
        y = x % s
else:
    if abs(x) > s:
        y = (s - (abs(x) % s)) % s
    else:
        y = s - abs(x)

print(y)