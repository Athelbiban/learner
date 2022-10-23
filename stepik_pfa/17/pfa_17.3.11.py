import re

with open('files/nums1.txt', encoding='utf-8') as inf:
    reg = re.findall(r'\d+', inf.read())
    print(sum(map(int, reg)))
