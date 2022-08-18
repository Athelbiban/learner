import re

s = input()
print(''.join(i[1] + str(len(i[0])) for i in re.finditer(r'([\w+])\1*', s)))
