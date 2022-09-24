import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

c = sum(matrix, [])
random.shuffle(c)
c = iter(c)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = next(c)
print(matrix)
