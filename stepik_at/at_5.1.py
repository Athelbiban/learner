import time

start = time.time()


def collatz_conjecture(n):
    print(n, end=' ')
    if n == 1:
        return
    elif n % 2:
        n = n * 3 + 1
    else:
        n = n // 2
    collatz_conjecture(n)


a = 97
if __name__ == '__main__':
    collatz_conjecture(a)
print()
print(time.time() - start)
