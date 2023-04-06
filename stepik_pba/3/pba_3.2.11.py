import re
import sys

sys.stdout.writelines(filter(re.compile(r'\b(\w+)\1\b').search, sys.stdin))
