number, unit_from, _, unit_to = input().split()
number = float(number)
info = {'mile': 1609,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001}

result = number * info[unit_from] / info[unit_to]

print(f'{result:.2e}')
