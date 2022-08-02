def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


if __name__ == '__main__':
    print(descending_order(13249))
