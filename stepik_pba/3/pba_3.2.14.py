import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    for word in re.findall(r'\b\w{2,}\b', line):
        line = re.sub(rf'\b{word}\b', f'{word[1]}{word[0]}{word[2:]}', line)
    print(line)
