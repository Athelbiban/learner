import re

s, f = input(), input()

## Вариант 1:
# if f in s:
#     print(*[m.start() for m in re.finditer(f'(?=({f}))', s)])
# else:
#     print(-1)


#Вариант 2:
print(*[m.start() for m in re.finditer(f'(?=({f}))', s)] or [-1])
