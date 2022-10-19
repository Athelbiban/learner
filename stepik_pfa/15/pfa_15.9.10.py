# print(all(map(lambda i: i[0]**2 + i[1]**2 + i[2]**2 <= 4, zip(*[map(float, input().split()) for _ in range(3)]))))
print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(*[map(float, input().split()) for _ in range(3)])))
