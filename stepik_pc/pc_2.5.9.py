s = '4 -1 9 3'
summ = 0
for i in s:
    summ += int(i)
print(summ)

# второй, читерский способ:

# print(eval('+'.join(input().split())))

# print(eval(s.replace(' ', '+')))

