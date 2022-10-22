import random as rnd

file = open('files/lines.txt', encoding='utf-8')
content = rnd.choice(file.readlines()).rstrip()
file.close()
print(content)
