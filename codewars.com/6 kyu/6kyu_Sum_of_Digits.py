def digital_root(n):
    s = [int(i) for i in str(n)]
    if len(s) == 1:
        return s[0]
    else:
        return digital_root(sum(s))


if __name__ == '__main__':
    print(digital_root(132189))
