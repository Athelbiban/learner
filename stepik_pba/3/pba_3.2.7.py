import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    if re.match(r'(.*cat){2,}', line):
        print(line)
