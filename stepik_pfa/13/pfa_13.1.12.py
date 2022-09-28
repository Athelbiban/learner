from decimal import *

num = Decimal(input())
a = num.as_tuple().digits
b = num.as_tuple().exponent
print(min(a) + max(a) if len(a) > abs(b) else max(a))
