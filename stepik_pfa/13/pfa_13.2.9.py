from fractions import Fraction as F

a, b = input(), input()

print(f'{a} + {b} = {F(a) + F(b)}',
      f'{a} - {b} = {F(a) - F(b)}',
      f'{a} * {b} = {F(a) * F(b)}',
      f'{a} / {b} = {F(a) / F(b)}', sep='\n')
