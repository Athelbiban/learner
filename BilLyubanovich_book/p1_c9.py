## 9.1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
#
#
# print(good())


## 9.2
# def get_odds(start=1, end=5, step=1):
#     ## Циклом "for":
#     # for e in range(start, end, step):
#     #     if e % 2:
#     #         yield e
#     # Циклом "while":
#     numb = start
#     while numb < end:
#         if numb % 2:
#             yield numb
#         numb += 1
#
#
# ranger = get_odds(0, 10)
# n = 1
# for i in ranger:
#     if n == 3:
#         print(i)
#         break
#     n += 1


# 9.3
# def test(func):
#     def new_func(*args):
#         print('start')
#         result = func(*args)
#         print('end')
#         return result
#     return new_func
#
#
# @test
# def greeting():
#     print('Hello, World!')
#
#
# greeting()

## Пример:
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Runniing function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
#
# @document_it
# def add_ints(a, b):
#     return a + b
#
#
# print(add_ints(3, 5))


# 9.4
# s = [1, 2, 3, 4, 5]
# while True:
#     value = input('Введите число от 1 до 5: ')
#     if value == '17':
#         break
#     try:
#         pos = int(value)
#         print(s[pos - 1])
#     except IndexError as OopsErr:
#         print('Я же сказал от 1 до 5! Ну что тут не ясно? А у вас тут такое:', pos)
#     except Exception as other:
#         print('Давайте посмотрим что тут у вас:', other)


class OopsException(Exception):
    pass


while True:
    word = input('Введите любое слово: ')
    if word == 'Stop':
        break
    elif word.isupper():
        try:
            raise OopsException('А чего это ты капсом на меня кричишь?')
        except OopsException as exc:
            print(exc)

