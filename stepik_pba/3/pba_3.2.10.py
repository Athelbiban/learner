import re
import sys

sys.stdout.writelines(filter(re.compile(r'\\').search, sys.stdin))
