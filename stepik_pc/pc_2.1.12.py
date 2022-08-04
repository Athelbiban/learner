a, b = int(input()), int(input())
i = 1
while not (i % a == 0 and i % b == 0):
    i += 1
print(i)
