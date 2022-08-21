import time

start = time.time()


def next_triangle_number(index_triangle_nuber):
    next_index = index_triangle_nuber + 1
    triangle_number = 0
    for i in range(1, next_index + 1):
        triangle_number += i
    return is_more_500_dividers(triangle_number, next_index)


def is_more_500_dividers(number, index):
    dividers = 0
    for e in range(1, number // 2):
        if not number % e:
            dividers += 1
    print(dividers)
    if dividers <= 500:
        next_triangle_number(index)
    return number


n, i = 1, 1

print(is_more_500_dividers(n, i))
end = time.time() - start
print(end)
