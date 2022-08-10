# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке,
# как показано в примере (здесь n=5):
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9


n = int(input())
table = [[0] * n for _ in range(n)]
checklist = list(range(1, n * n + 1))
row, col, k = 0, 0, 0

while len(checklist) > 1:
    for i in range(k, n - k):
        col = i
        table[row][col] = checklist[0]
        del checklist[0]
    for i in range(k + 1, n - k):
        row = i
        table[row][col] = checklist[0]
        del checklist[0]
    for i in range(n - 2 - k, -1 + k, -1):
        col = i
        table[row][col] = checklist[0]
        del checklist[0]
    for i in range(n - 2 - k, 0 + k, -1):
        row = i
        table[row][col] = checklist[0]
        del checklist[0]
    k += 1
if n % 2:
    table[n // 2][(n - 1) // 2] = checklist[0]
    del checklist[0]

for i in table:
    print(*i)
