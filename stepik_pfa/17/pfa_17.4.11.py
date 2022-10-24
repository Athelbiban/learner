with open('files/class_scores.txt', encoding='utf-8') as inf, open('files/new_scores.txt', 'w', encoding='utf-8') as ouf:
    print(*[f'{a} {int(b) + 5 if int(b) <= 95 else 100}' for line in inf for a, b in [line.split()]], sep='\n', file=ouf)
