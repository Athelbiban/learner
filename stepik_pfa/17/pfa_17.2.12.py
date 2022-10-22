file = open(input(), encoding='utf-8')
print(list(file)[-2].rstrip())
file.close()
