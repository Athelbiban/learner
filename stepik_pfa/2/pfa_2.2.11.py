import re

s = f'{input()} запретил букву'
a = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for i in a:
    if i in s:
        print(s, i)
        s = ''.join(re.split(i, s)).strip().replace('  ', ' ')
