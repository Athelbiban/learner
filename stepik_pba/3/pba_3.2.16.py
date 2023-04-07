import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    reg = re.findall(r'[1|0]', line)
    if ''.join(reg) == line:
        sum_even = 0
        sum_odd = 0
        for i, e in enumerate(reg[::-1], 1):
            if i % 2:
                sum_odd += int(e)
            else:
                sum_even += int(e)
        if not (sum_even - sum_odd) % 3:
            print(line)
