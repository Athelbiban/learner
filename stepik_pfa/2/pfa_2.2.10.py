import re

# Вариант 1:
for i in range(1, int(input()) + 1):
    if re.findall(r"(a).*(n).*(t).*(o).*(n)", input()):
        print(i, end=' ')


# # Вариант 2:
# import re
#
# print(*[i for i in range(1, int(input()) + 1) if re.search(r"a.*n.*t.*o.*n", input())])
