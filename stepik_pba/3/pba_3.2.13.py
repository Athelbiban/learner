import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\ba+\b', 'argh', line, 1, re.IGNORECASE))
