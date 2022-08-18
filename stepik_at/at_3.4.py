dict_my = {}

for word in input().split():
    dict_my[word.lower()] = dict_my.get(word.lower(), 0) + 1
    print(word.lower(), dict_my[word.lower()])

