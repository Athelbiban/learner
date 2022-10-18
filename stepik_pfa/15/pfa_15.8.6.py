func = lambda i: i[0].lower() == 'a' == i[-1].lower()

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))
