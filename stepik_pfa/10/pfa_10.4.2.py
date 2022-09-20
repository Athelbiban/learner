dict1 = {}
dict2 = {}

for i in input():
    dict1[i] = dict1.get(i, 0) + 1

for e in input():
    dict2[e] = dict2.get(e, 0) + 1

print('YES' if dict1 == dict2 else 'NO')
