#  Нормальный вариант решения:
def add_binary(a, b):
    return bin(a + b)[2:]

# # Ненормальный вариант решения, но зато рабочий и через рекурсию:
# def add_binary(a, b, result=''):
#     s = a + b
#     if s == 0:
#         return result
#     else:
#         result = str(s % 2) + result
#         return add_binary(s // 2, 0, result=result)


if __name__ == '__main__':
    print(add_binary(1, 1))
