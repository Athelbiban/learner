def closest_mod_5(x):
    while x % 5:
        x += 1
    return x


if __name__ == '__main__':
    print(closest_mod_5(17))
