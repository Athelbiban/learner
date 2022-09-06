def find_it(seq):
    counter = 1
    odd = None
    for i in sorted(seq):
        if i == odd:
            counter += 1
        elif i != odd and odd is not None and counter % 2:
            return odd
        else:
            odd = i
            counter = 1
    return odd


if __name__ == '__main__':
    print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
