def pascal(n):
    c = [1]
    for k in range(1, n // 2 + 1):
        c.append(c[k - 1] * (n - k + 1) // k)
    return c + c[::-1] if n % 2 else c + c[-2::-1]


def main(n):
    for i in range(n):
        print(*pascal(i))


if __name__ == "__main__":
    main(int(input()))
