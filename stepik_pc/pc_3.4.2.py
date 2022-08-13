import re

with open(r'c:\Users\Станислав Олегович\Desktop\test\dataset_3363_2.txt', 'r') as inf:
    s = ''.join([i[0][0] * int(i[0][1:]) for i in re.finditer(r'\w\d+', inf.readline().strip())])

with open(r'c:\Users\Станислав Олегович\Desktop\test\dataset_3363_2.txt', 'w') as c:
    c.write(s)
