import re

s, n = input(), int(input())
# print([[e for e in i.group(0) if e != ' '] for i in re.finditer(rf'(.{n * 2})\1*', s + ' ')])
k = f'{f"{n*2}"}'
reg = re.finditer('(.{4})\\1*', s + ' ')
# print([[e for e in i.group(10)] for i in reg])
print(reg)

for i in reg:
    print(i.group(0))
