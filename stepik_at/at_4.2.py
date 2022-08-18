s = input()
h = ''
n = 0
for i in range(len(s)):
    if not s[i].isdigit():
        if s[n:i]:
            h += s[i] * int(s[n:i])
        else:
            h += s[i]
        n = i + 1
print(h)
