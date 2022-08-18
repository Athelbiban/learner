# s = """Duck - %s,
# Pumpkin - %s,
# Pomeranian - %s."""
# print(s % d)

# s1 = """Duck - {0[0]},
# Pumpkin - {0[1]},
# Pomeranian - {0[2]}."""
# d = 'Ducky McDuckface', 'Pumpkiny McPumpkinface', 'Pomeraniany McPomeranianface'
# print(s1.format(d))

# s2 = """Duck - {},
# Pumpkin - {},
# Pomeranian - {}."""
# print(s2.format('Ducky McDuckface', 'Pumpkiny McPumpkinface', 'Pomeraniany McPomeranianface'))

# s3 = """Duck - {duck},
# Pumpkin - {pum},
# Pomeranian - {pom}."""
# print(s3.format(duck='Ducky McDuckface', pum='Pumpkiny McPumpkinface', pom='Pomeraniany McPomeranianface'))

# s3 = """Duck - {0[duck]},
# Pumpkin - {0[pum]},
# Pomeranian - {0[pom]}."""
# d = {'duck': 'Ducky McDuckface',
#      'pum': 'Pumpkiny McPumpkinface',
#      'pom': 'Pomeraniany McPomeranianface'
#      }
# print(s3.format(d))

duck = 'Ducky McDuckface'
pum = 'Pumpkiny McPumpkinface'
pom = 'Pomeraniany McPomeranianface'
print(f'''Duck - {duck},\nPumpkin - {pum},\nPomeranian - {pom}.''')

print(f'''Duck - {duck},
Pumpkin - {pum},
Pomeranian - {pom}.''')
