numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

# result = {k: [] for k in numbers}
# for k in numbers:
#     if not result[k]:
#         for i in range(1, k + 1):
#             if not k % i:
#                 result.setdefault(k).append(i)
# print(result)

result = {k: [v for v in range(1, k + 1) if not k % v] for k in numbers}
print(result)
