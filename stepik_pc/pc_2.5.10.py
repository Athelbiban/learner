s = input().split()
result = ''

for i in range(len(s)):
    if len(s) == 1:
        result = s[i]
        break
    if i == 0:
        result += str(int(s[-1]) + int(s[i + 1])) + ' '
    elif i == len(s) - 1:
        result += str(int(s[i - 1]) + int(s[0])) + ' '
    else:
        result += str(int(s[i - 1]) + int(s[i + 1])) + ' '

print(result)
