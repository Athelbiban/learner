import re

s = 0
for i in re.finditer(r'\Р+', input()):
    if s < len(i[0]):
        s = len(i[0])
print(s)

# # Вариант 2 для ленивых:
# print(len(max(input().split('О'))))
