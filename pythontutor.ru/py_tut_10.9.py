"""
Задача «Полиглоты»
Условие
Каждый из некоторого множества школьников некоторой школы знает
некоторое количество языков. Нужно определить сколько языков знают все
школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников
сперва записано количество языков, которое он знает, а затем - названия
языков, по одному в строке.

В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""


number_schoolboy = int(input())
max_languages, common_language = set(), set()

for i in range(number_schoolboy):
    number_languages = int(input())
    set_languages = set()
    for j in range(number_languages):
        set_languages.add(input())
        max_languages |= set_languages
    if len(common_language) == 0:
        common_language |= set_languages
    else:
        common_language &= set_languages

print(len(common_language)), print(*sorted([i for i in common_language]), sep='\n')
print(len(max_languages)), print(*sorted([i for i in max_languages]), sep='\n')
