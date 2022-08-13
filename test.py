import os.path

# Чтение из файла

inf = open('file.txt', 'r')
s1 = inf.readline()
s2 = inf.readline()
inf.close()

with open('file.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

# Полезные функции

s = inf.readline().strip()

os.path.join('.', 'dirname', 'filename.txt')
r'.\dirname\filename.txt'

# Запись в файл

ouf = open('file.txt', 'w')
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

with open('file.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))

