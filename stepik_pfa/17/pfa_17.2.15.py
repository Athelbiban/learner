file = open('files/nums.txt', encoding='utf-8')
print(sum(map(int, file.read().split())))
# print(sum(map(int, filter(lambda i: i.strip().isdigit(), file.readlines()))))
file.close()
