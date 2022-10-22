file = open('files/prices.txt', encoding='utf-8')
content = map(str.split, file)
print(sum(map(lambda i: int(i[1]) * int(i[2]), content)))
file.close()
