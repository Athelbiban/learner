n, m = map(int, input().split())

for i in range(n, m + 1):
    print('FizzBuzz' if not i % 3 and not i % 5 else 'Fizz' if not i % 3 else 'Buzz' if not i % 5 else i)
