s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana ' \
    'banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana' \
    'grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime' \
    'quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana' \
    'quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate' \
    'banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon' \
    'pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
d = {}

for word in s:
    d[word] = d.get(word, 0) + 1
lst = sorted(d.items(), key=lambda x: x[1], reverse=True)
lst2 = []
n = 0
for k, v in lst:
    if v < n:
        break
    lst2.append(k)
    n = v
print(sorted(lst2)[0])
