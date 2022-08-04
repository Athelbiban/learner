import time

start = time.time()


# def triple():    # мой первый доработанный код (время ~ 1.2 сек.), до доработки ~ 10 сек.
#     for c in range(3, 1000):
#         for b in range(2, c):
#             for a in range(1, b):
#                 if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                     return f'a = {a}; b = {b}; c = {c}; a * b * c = {a * b * c}.'
#
#
# if __name__ == '__main__':
#     print(triple())


# def main():   # код того парня с GitHub (время ~ 0.00 сек.)
#     final_sum = 0
#     a, b, c = 0, 0, 0
#     for m in range(2, 500):
#         print(m)
#         for n in range(1, m):
#             print(n)
#             # EURIKA!
#             if 2*m*n + 2*m*m == 1000:
#                 a, b, c = 2*m*n, m*m - n*n, m*m + n*n
#                 print(a, b, c)
#                 print(a*b*c)
#                 return

# if __name__ == "__main__":
#    main()


def main():     # мой второй доработанный код (время ~ 0.04 сек.)
    for m in range(2, 1000):
        print(m)
        for n in range(1, m):
            print(n)
            if n + m + (m * m + n * n) ** 0.5 == 1000:
                a, b, c = n, m, int((m * m + n * n) ** 0.5)
                return f'a = {a}; b = {b}; c = {c}; a * b * c = {a * b * c}.'


if __name__ == '__main__':
    print(main())


end = time.time()
print('Время выполнения: {:.2f} сек. (~ {:.1f} мин.)'.format((end - start), ((end - start) / 60)))
