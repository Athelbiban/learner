print(*filter(lambda i: '0' not in str(i) and all(i % int(b) == 0 for b in str(i)),
              range(int(input()), int(input()) + 1)))
