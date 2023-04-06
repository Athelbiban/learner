import re
import sys


sys.stdout.writelines(re.sub('human', 'computer', sys.stdin.read()))