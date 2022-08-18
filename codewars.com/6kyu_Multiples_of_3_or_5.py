# # Вариант 1:
# def solution(number):
#     result = 0
#     for i in range(1, number):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result
#
#
# if __name__ == '__main__':
#     print(solution(-13))


# Вариант 2:
def solution(number):
    return sum(i for i in range(1, number) if i % 3 == 0 or i % 5 == 0)


if __name__ == '__main__':
    print(solution(3))
