"""
Задача «Самое частое слово»
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте
встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""


d = {}
l = []
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1
l2 = sorted(d.items(), key=lambda x: x[1], reverse=True)
for word, count in l2:
    if d[word] >= l2[0][1]:
        l += [word]
print(sorted(l)[0])
