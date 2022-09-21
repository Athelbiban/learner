words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {k: [ord(v) for v in k] for k in words}
print(result)
