x, y = 0, 0

for _ in range(int(input())):
    direction, shift = input().split()
    shift = int(shift)
    y = y + shift if direction == 'север' else y - shift if direction == 'юг' else y
    x = x + shift if direction == 'восток' else x - shift if direction == 'запад' else x

print(x, y)
