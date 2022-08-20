sequence = list(map(int, input().split()))
scope = range(1, len(sequence))
print('Jolly' if sorted([abs(sequence[i] - sequence[i-1]) for i in scope]) == list(scope) else 'Not jolly')
