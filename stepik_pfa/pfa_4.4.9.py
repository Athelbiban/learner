n, m = int(input()), int(input())
lst = [[input() for a in range(m)] for b in range(n)]


# for i in range(n):
#     for j in range(m):
#         print(lst[i][j], end=' ')
#     print()
# print()
# for i in range(m):
#     for j in range(n):
#         print(lst[j][i], end=' ')
#     print()


transposed_lst = [list(i) for i in zip(*lst)]
[print(*i) for i in lst]
print()
[print(*i) for i in transposed_lst]
