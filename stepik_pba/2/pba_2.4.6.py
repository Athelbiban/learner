import os.path
import re


os.chdir(r'c:\Users\VostrovSO\Downloads')
reg = re.compile(r'\.py$')
list_dir = []
for path, dirs, files in os.walk('main'):
    for file in files:
        if reg.search(file):
            list_dir.append(path)
            break

with open(r'ans.txt', 'w', encoding='utf-8') as ouf:
    ouf.write('\n'.join(sorted(list_dir)))
