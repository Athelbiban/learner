# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
# После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
# первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
#
# Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
#
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1
#
# Sample Input 2:
# 1
# end
#
# Sample Output 2:
# 4


counter, s, x = 0, [], []
n = input()

while n != 'end':
    s.append([int(i) for i in n.split()])
    n = input()
    counter += 1

k = [[] for t in range(counter)]

for j, u in enumerate(s):
    for i, _ in enumerate(u):
        x.append(s[j - 1][i] + s[(j + 1) % len(s)][i] + s[j][i - 1] + s[j][(i + 1) % len(s[0])])

for e in range(counter):
    c = 0
    for g in x:
        k[e].append(g)
        c += 1
        if c >= len(s[0]):
            break
    del x[:len(s[0])]

for _, b in enumerate(k):
    print(*b)
