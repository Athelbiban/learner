s = [int(input()) for _ in range(int(input()))]
composition = int(input())

for i, e in enumerate(s):
    for k in range(i + 1, len(s)):
        if e * s[k] == composition:
            exit(print("ДА"))
print("НЕТ")


# # Вариант без вложенных циклов:
# n = int(input())
# s = [int(input()) for _ in range(n)]
# composition = int(input())
# counter = 0
# for i in s:
#     if i != 0 and int(composition / i) in s:
#         counter += 1
#     if counter > 1:
#         print("ДА")
#         break
# else:
#     print("НЕТ")
