def sort_pair(couple):
    (a, b) = couple
    if a <= b:
        return (a, b)
    else:
        return (b, a)


print(sort_pair((5, 1)))
print(sort_pair((2, 2)))
print(sort_pair((7, 8)))

