def move_zeros(lst):
    lst1 = []
    while 0 in lst:
        lst1.append(lst.pop(lst.index(0)))
    lst.extend(lst1)
    return lst


if __name__ == '__main__':
    print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
