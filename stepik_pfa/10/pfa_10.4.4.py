d = {k: v for _ in range(int(input())) for k, v in [input().split()]}
b = {v: k for k, v in d.items()}
word = input()
print(d.get(word, b.get(word)))
