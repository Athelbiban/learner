from collections import Counter

rating_log = input().split()
count = Counter(rating_log)
print(f'{count["A"] / len(rating_log):.2f}')
